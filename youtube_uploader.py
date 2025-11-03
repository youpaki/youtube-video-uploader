#!/usr/bin/env python3
"""
YouTube Video Uploader
Automatically uploads videos from specified folders to YouTube
"""

import os
import sys
import pickle
import argparse
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

# YouTube API scopes
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

# Supported video formats
VIDEO_EXTENSIONS = {'.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm', '.m4v', '.mpeg', '.mpg'}

class YouTubeUploader:
    def __init__(self, credentials_file='credentials.json', token_file='token.pickle'):
        """Initialize the YouTube uploader with authentication"""
        self.credentials_file = credentials_file
        self.token_file = token_file
        self.youtube = None
        
    def authenticate(self):
        """Authenticate with YouTube API using OAuth2"""
        creds = None
        
        # Load saved credentials if available
        if os.path.exists(self.token_file):
            print("Loading saved credentials...")
            with open(self.token_file, 'rb') as token:
                creds = pickle.load(token)
        
        # If credentials are invalid or don't exist, get new ones
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                print("Refreshing access token...")
                creds.refresh(Request())
            else:
                if not os.path.exists(self.credentials_file):
                    print(f"\nERROR: {self.credentials_file} not found!")
                    print("\nTo use this application, you need to:")
                    print("1. Go to https://console.cloud.google.com/")
                    print("2. Create a new project (or select existing)")
                    print("3. Enable YouTube Data API v3")
                    print("4. Create OAuth 2.0 credentials (Desktop app)")
                    print("5. Download the credentials and save as 'credentials.json'")
                    print("6. Place credentials.json in the same folder as this script\n")
                    sys.exit(1)
                
                print("Starting authentication flow...")
                print("A browser window will open for you to authorize the application.")
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Save credentials for future use
            with open(self.token_file, 'wb') as token:
                pickle.dump(creds, token)
            print("Credentials saved successfully!")
        
        # Build the YouTube API client
        self.youtube = build('youtube', 'v3', credentials=creds)
        print("✓ Successfully authenticated with YouTube!\n")
        
    def upload_video(self, video_path, title=None, description="", category="22", 
                    privacy="private", tags=None):
        """
        Upload a video to YouTube
        
        Args:
            video_path: Path to the video file
            title: Video title (defaults to filename)
            description: Video description
            category: YouTube category ID (22 = People & Blogs)
            privacy: Privacy status (public, private, unlisted)
            tags: List of tags
        """
        if not self.youtube:
            raise Exception("Not authenticated. Call authenticate() first.")
        
        video_path = Path(video_path)
        if not video_path.exists():
            raise FileNotFoundError(f"Video file not found: {video_path}")
        
        # Use filename as title if not provided
        if title is None:
            title = video_path.stem
        
        # Prepare video metadata
        body = {
            'snippet': {
                'title': title,
                'description': description,
                'categoryId': category
            },
            'status': {
                'privacyStatus': privacy,
                'selfDeclaredMadeForKids': False
            }
        }
        
        if tags:
            body['snippet']['tags'] = tags
        
        # Create MediaFileUpload object
        media = MediaFileUpload(
            str(video_path),
            chunksize=-1,  # Upload in a single request
            resumable=True
        )
        
        try:
            print(f"Uploading: {video_path.name}")
            print(f"Title: {title}")
            print(f"Privacy: {privacy}")
            
            # Execute the upload
            request = self.youtube.videos().insert(
                part=','.join(body.keys()),
                body=body,
                media_body=media
            )
            
            response = None
            while response is None:
                status, response = request.next_chunk()
                if status:
                    progress = int(status.progress() * 100)
                    print(f"Upload progress: {progress}%", end='\r')
            
            print(f"\n✓ Successfully uploaded: {title}")
            print(f"  Video ID: {response['id']}")
            print(f"  URL: https://www.youtube.com/watch?v={response['id']}\n")
            
            return response
            
        except HttpError as e:
            print(f"\n✗ Error uploading {video_path.name}: {e}")
            return None
        except Exception as e:
            print(f"\n✗ Unexpected error uploading {video_path.name}: {e}")
            return None
    
    def upload_from_folders(self, folders, recursive=False, privacy="private", 
                          description="", category="22", tags=None):
        """
        Upload all videos from specified folders
        
        Args:
            folders: List of folder paths
            recursive: Whether to search subfolders
            privacy: Privacy status for uploaded videos
            description: Description for uploaded videos
            category: YouTube category ID
            tags: Tags for uploaded videos
        """
        video_files = []
        
        # Collect all video files from folders
        for folder in folders:
            folder_path = Path(folder)
            if not folder_path.exists():
                print(f"Warning: Folder not found: {folder}")
                continue
            
            if not folder_path.is_dir():
                print(f"Warning: Not a directory: {folder}")
                continue
            
            print(f"Scanning folder: {folder_path}")
            
            if recursive:
                # Search recursively
                for ext in VIDEO_EXTENSIONS:
                    video_files.extend(folder_path.rglob(f"*{ext}"))
            else:
                # Search only in the specified folder
                for ext in VIDEO_EXTENSIONS:
                    video_files.extend(folder_path.glob(f"*{ext}"))
        
        if not video_files:
            print("No video files found in specified folders.")
            return
        
        print(f"\nFound {len(video_files)} video(s) to upload\n")
        print("=" * 60)
        
        uploaded = 0
        failed = 0
        
        for i, video_file in enumerate(video_files, 1):
            print(f"\n[{i}/{len(video_files)}]")
            result = self.upload_video(
                video_file,
                privacy=privacy,
                description=description,
                category=category,
                tags=tags
            )
            
            if result:
                uploaded += 1
            else:
                failed += 1
        
        print("=" * 60)
        print(f"\nUpload complete!")
        print(f"  Successful: {uploaded}")
        print(f"  Failed: {failed}")
        print(f"  Total: {len(video_files)}")


def main():
    parser = argparse.ArgumentParser(
        description='Upload videos from folders to YouTube',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Upload videos from a single folder:
    python youtube_uploader.py "C:\\Videos\\MyVideos"
  
  Upload from multiple folders:
    python youtube_uploader.py "C:\\Videos\\Folder1" "D:\\More Videos"
  
  Upload with custom settings:
    python youtube_uploader.py "C:\\Videos" --privacy public --recursive
    
  Upload as unlisted with description:
    python youtube_uploader.py "C:\\Videos" --privacy unlisted --description "My video description"
        """
    )
    
    parser.add_argument(
        'folders',
        nargs='+',
        help='One or more folder paths containing videos to upload'
    )
    
    parser.add_argument(
        '-r', '--recursive',
        action='store_true',
        help='Search subfolders recursively'
    )
    
    parser.add_argument(
        '-p', '--privacy',
        choices=['public', 'private', 'unlisted'],
        default='private',
        help='Privacy status for uploaded videos (default: private)'
    )
    
    parser.add_argument(
        '-d', '--description',
        default='',
        help='Description for uploaded videos'
    )
    
    parser.add_argument(
        '-c', '--category',
        default='22',
        help='YouTube category ID (default: 22 = People & Blogs)'
    )
    
    parser.add_argument(
        '-t', '--tags',
        nargs='*',
        help='Tags for uploaded videos'
    )
    
    parser.add_argument(
        '--credentials',
        default='credentials.json',
        help='Path to credentials file (default: credentials.json)'
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("YouTube Video Uploader")
    print("=" * 60)
    print()
    
    # Initialize uploader
    uploader = YouTubeUploader(credentials_file=args.credentials)
    
    # Authenticate
    try:
        uploader.authenticate()
    except Exception as e:
        print(f"Authentication failed: {e}")
        sys.exit(1)
    
    # Upload videos
    uploader.upload_from_folders(
        folders=args.folders,
        recursive=args.recursive,
        privacy=args.privacy,
        description=args.description,
        category=args.category,
        tags=args.tags
    )


if __name__ == '__main__':
    main()
