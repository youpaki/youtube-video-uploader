#!/usr/bin/env python3
"""
YouTube Video Uploader - GUI Version
Graphical interface for uploading videos to YouTube
"""

import os
import sys
import pickle
import threading
from pathlib import Path
from tkinter import Tk, Frame, Label, Entry, Button, Text, Scrollbar, Listbox
from tkinter import filedialog, messagebox, ttk
from tkinter import StringVar, IntVar, BooleanVar, END, WORD, VERTICAL, HORIZONTAL
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

# YouTube API scopes
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

# Supported video formats
VIDEO_EXTENSIONS = {'.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm', '.m4v', '.mpeg', '.mpg'}

# YouTube categories
YOUTUBE_CATEGORIES = {
    "Film & Animation": "1",
    "Autos & Vehicles": "2",
    "Music": "10",
    "Pets & Animals": "15",
    "Sports": "17",
    "Travel & Events": "19",
    "Gaming": "20",
    "People & Blogs": "22",
    "Comedy": "23",
    "Entertainment": "24",
    "News & Politics": "25",
    "Howto & Style": "26",
    "Education": "27",
    "Science & Technology": "28",
    "Nonprofits & Activism": "29"
}


class YouTubeUploaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Uploader")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Variables
        self.folders = []
        self.video_files = []
        self.youtube = None
        self.credentials_file = 'credentials.json'
        self.token_file = 'token.pickle'
        self.is_uploading = False
        
        # Setup UI
        self.setup_ui()
        
    def setup_ui(self):
        """Create the user interface"""
        # Main container
        main_frame = Frame(self.root, padx=10, pady=10)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = Label(main_frame, text="YouTube Video Uploader", 
                           font=('Arial', 16, 'bold'))
        title_label.pack(pady=(0, 10))
        
        # Authentication Section
        auth_frame = Frame(main_frame, relief='ridge', borderwidth=2, padx=10, pady=10)
        auth_frame.pack(fill='x', pady=(0, 10))
        
        Label(auth_frame, text="Authentication", font=('Arial', 12, 'bold')).pack(anchor='w')
        
        auth_button_frame = Frame(auth_frame)
        auth_button_frame.pack(fill='x', pady=5)
        
        self.auth_status_label = Label(auth_button_frame, text="Not authenticated", 
                                       fg='red', font=('Arial', 10))
        self.auth_status_label.pack(side='left', padx=5)
        
        Button(auth_button_frame, text="Authenticate with YouTube", 
               command=self.authenticate, bg='#4CAF50', fg='white',
               font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        
        # Folder Selection Section
        folder_frame = Frame(main_frame, relief='ridge', borderwidth=2, padx=10, pady=10)
        folder_frame.pack(fill='both', expand=True, pady=(0, 10))
        
        Label(folder_frame, text="Video Folders", font=('Arial', 12, 'bold')).pack(anchor='w')
        
        folder_button_frame = Frame(folder_frame)
        folder_button_frame.pack(fill='x', pady=5)
        
        Button(folder_button_frame, text="Add Folder", 
               command=self.add_folder, bg='#2196F3', fg='white',
               font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        
        Button(folder_button_frame, text="Clear All", 
               command=self.clear_folders, bg='#f44336', fg='white',
               font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        
        self.recursive_var = BooleanVar(value=False)
        ttk.Checkbutton(folder_button_frame, text="Search subfolders recursively", 
                       variable=self.recursive_var, 
                       command=self.scan_videos).pack(side='left', padx=10)
        
        # Folder list
        folder_list_frame = Frame(folder_frame)
        folder_list_frame.pack(fill='both', expand=True, pady=5)
        
        folder_scrollbar = Scrollbar(folder_list_frame)
        folder_scrollbar.pack(side='right', fill='y')
        
        self.folder_listbox = Listbox(folder_list_frame, yscrollcommand=folder_scrollbar.set,
                                      height=4)
        self.folder_listbox.pack(side='left', fill='both', expand=True)
        folder_scrollbar.config(command=self.folder_listbox.yview)
        
        # Video Summary Section
        summary_frame = Frame(main_frame, relief='ridge', borderwidth=2, padx=10, pady=10)
        summary_frame.pack(fill='both', expand=True, pady=(0, 10))
        
        Label(summary_frame, text="Videos to Upload", font=('Arial', 12, 'bold')).pack(anchor='w')
        
        self.video_count_label = Label(summary_frame, text="No videos found", 
                                       font=('Arial', 10))
        self.video_count_label.pack(anchor='w', pady=5)
        
        # Video list
        video_list_frame = Frame(summary_frame)
        video_list_frame.pack(fill='both', expand=True, pady=5)
        
        video_scrollbar = Scrollbar(video_list_frame)
        video_scrollbar.pack(side='right', fill='y')
        
        self.video_listbox = Listbox(video_list_frame, yscrollcommand=video_scrollbar.set,
                                     height=6)
        self.video_listbox.pack(side='left', fill='both', expand=True)
        video_scrollbar.config(command=self.video_listbox.yview)
        
        # Upload Settings Section
        settings_frame = Frame(main_frame, relief='ridge', borderwidth=2, padx=10, pady=10)
        settings_frame.pack(fill='x', pady=(0, 10))
        
        Label(settings_frame, text="Upload Settings", font=('Arial', 12, 'bold')).pack(anchor='w')
        
        # Privacy setting
        privacy_frame = Frame(settings_frame)
        privacy_frame.pack(fill='x', pady=5)
        
        Label(privacy_frame, text="Privacy:", width=15, anchor='w').pack(side='left')
        
        self.privacy_var = StringVar(value='private')
        privacy_options = Frame(privacy_frame)
        privacy_options.pack(side='left')
        
        ttk.Radiobutton(privacy_options, text="Private", variable=self.privacy_var, 
                       value='private').pack(side='left', padx=5)
        ttk.Radiobutton(privacy_options, text="Unlisted", variable=self.privacy_var, 
                       value='unlisted').pack(side='left', padx=5)
        ttk.Radiobutton(privacy_options, text="Public", variable=self.privacy_var, 
                       value='public').pack(side='left', padx=5)
        
        # Description
        desc_frame = Frame(settings_frame)
        desc_frame.pack(fill='x', pady=5)
        
        Label(desc_frame, text="Description:", width=15, anchor='w').pack(side='left')
        self.description_entry = Entry(desc_frame)
        self.description_entry.pack(side='left', fill='x', expand=True, padx=(0, 5))
        
        # Tags
        tags_frame = Frame(settings_frame)
        tags_frame.pack(fill='x', pady=5)
        
        Label(tags_frame, text="Tags (comma-separated):", width=15, anchor='w').pack(side='left')
        self.tags_entry = Entry(tags_frame)
        self.tags_entry.pack(side='left', fill='x', expand=True, padx=(0, 5))
        
        # Category
        category_frame = Frame(settings_frame)
        category_frame.pack(fill='x', pady=5)
        
        Label(category_frame, text="Category:", width=15, anchor='w').pack(side='left')
        self.category_var = StringVar(value="People & Blogs")
        category_dropdown = ttk.Combobox(category_frame, textvariable=self.category_var,
                                         values=list(YOUTUBE_CATEGORIES.keys()),
                                         state='readonly', width=30)
        category_dropdown.pack(side='left')
        
        # Progress Section
        progress_frame = Frame(main_frame, relief='ridge', borderwidth=2, padx=10, pady=10)
        progress_frame.pack(fill='both', expand=True, pady=(0, 10))
        
        Label(progress_frame, text="Progress", font=('Arial', 12, 'bold')).pack(anchor='w')
        
        self.progress_label = Label(progress_frame, text="Ready to upload", 
                                    font=('Arial', 10))
        self.progress_label.pack(anchor='w', pady=5)
        
        self.progress_bar = ttk.Progressbar(progress_frame, mode='determinate', length=400)
        self.progress_bar.pack(fill='x', pady=5)
        
        # Log text area
        log_frame = Frame(progress_frame)
        log_frame.pack(fill='both', expand=True, pady=5)
        
        log_scrollbar = Scrollbar(log_frame)
        log_scrollbar.pack(side='right', fill='y')
        
        self.log_text = Text(log_frame, height=8, yscrollcommand=log_scrollbar.set,
                            wrap=WORD, state='disabled')
        self.log_text.pack(side='left', fill='both', expand=True)
        log_scrollbar.config(command=self.log_text.yview)
        
        # Upload Button
        button_frame = Frame(main_frame)
        button_frame.pack(fill='x')
        
        self.upload_button = Button(button_frame, text="Start Upload", 
                                    command=self.start_upload,
                                    bg='#4CAF50', fg='white',
                                    font=('Arial', 12, 'bold'),
                                    height=2)
        self.upload_button.pack(fill='x')
        
    def log(self, message):
        """Add message to log"""
        self.log_text.config(state='normal')
        self.log_text.insert(END, message + '\n')
        self.log_text.see(END)
        self.log_text.config(state='disabled')
        
    def authenticate(self):
        """Authenticate with YouTube API"""
        self.log("Starting authentication...")
        
        try:
            creds = None
            
            # Load saved credentials if available
            if os.path.exists(self.token_file):
                with open(self.token_file, 'rb') as token:
                    creds = pickle.load(token)
            
            # If credentials are invalid or don't exist, get new ones
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    if not os.path.exists(self.credentials_file):
                        messagebox.showerror("Error", 
                            f"{self.credentials_file} not found!\n\n"
                            "Please:\n"
                            "1. Go to https://console.cloud.google.com/\n"
                            "2. Create OAuth 2.0 credentials (Desktop app)\n"
                            "3. Download and save as 'credentials.json'")
                        return
                    
                    flow = InstalledAppFlow.from_client_secrets_file(
                        self.credentials_file, SCOPES)
                    creds = flow.run_local_server(port=0)
                
                # Save credentials
                with open(self.token_file, 'wb') as token:
                    pickle.dump(creds, token)
            
            # Build YouTube API client
            self.youtube = build('youtube', 'v3', credentials=creds)
            
            self.auth_status_label.config(text="✓ Authenticated", fg='green')
            self.log("Successfully authenticated with YouTube!")
            messagebox.showinfo("Success", "Successfully authenticated with YouTube!")
            
        except Exception as e:
            self.log(f"Authentication failed: {e}")
            messagebox.showerror("Authentication Error", str(e))
    
    def add_folder(self):
        """Add folder to list"""
        folder = filedialog.askdirectory(title="Select folder containing videos")
        if folder and folder not in self.folders:
            self.folders.append(folder)
            self.folder_listbox.insert(END, folder)
            self.scan_videos()
            
    def clear_folders(self):
        """Clear all folders"""
        self.folders = []
        self.folder_listbox.delete(0, END)
        self.video_files = []
        self.video_listbox.delete(0, END)
        self.video_count_label.config(text="No videos found")
        
    def scan_videos(self):
        """Scan folders for video files"""
        self.video_files = []
        self.video_listbox.delete(0, END)
        
        recursive = self.recursive_var.get()
        
        for folder in self.folders:
            folder_path = Path(folder)
            if not folder_path.exists():
                continue
            
            if recursive:
                for ext in VIDEO_EXTENSIONS:
                    self.video_files.extend(folder_path.rglob(f"*{ext}"))
            else:
                for ext in VIDEO_EXTENSIONS:
                    self.video_files.extend(folder_path.glob(f"*{ext}"))
        
        # Update UI
        if self.video_files:
            self.video_count_label.config(
                text=f"Found {len(self.video_files)} video(s) to upload"
            )
            for video in self.video_files:
                self.video_listbox.insert(END, video.name)
        else:
            self.video_count_label.config(text="No videos found")
            
    def start_upload(self):
        """Start upload process"""
        if self.is_uploading:
            messagebox.showwarning("Warning", "Upload already in progress!")
            return
            
        if not self.youtube:
            messagebox.showerror("Error", "Please authenticate first!")
            return
            
        if not self.video_files:
            messagebox.showerror("Error", "No videos to upload!")
            return
        
        # Confirm upload
        privacy = self.privacy_var.get()
        confirm = messagebox.askyesno(
            "Confirm Upload",
            f"Upload {len(self.video_files)} video(s) as '{privacy}'?\n\n"
            "This action cannot be undone."
        )
        
        if not confirm:
            return
        
        # Start upload in separate thread
        self.is_uploading = True
        self.upload_button.config(state='disabled', text="Uploading...", bg='#999')
        
        thread = threading.Thread(target=self.upload_videos)
        thread.daemon = True
        thread.start()
        
    def upload_videos(self):
        """Upload all videos"""
        privacy = self.privacy_var.get()
        description = self.description_entry.get()
        tags_text = self.tags_entry.get()
        tags = [tag.strip() for tag in tags_text.split(',')] if tags_text else None
        category = YOUTUBE_CATEGORIES[self.category_var.get()]
        
        total = len(self.video_files)
        uploaded = 0
        failed = 0
        
        self.progress_bar['maximum'] = total
        
        for i, video_file in enumerate(self.video_files, 1):
            self.progress_label.config(text=f"Uploading {i}/{total}: {video_file.name}")
            self.log(f"\n[{i}/{total}] Uploading: {video_file.name}")
            
            try:
                result = self.upload_video(
                    video_file,
                    privacy=privacy,
                    description=description,
                    category=category,
                    tags=tags
                )
                
                if result:
                    uploaded += 1
                    self.log(f"✓ Success! Video ID: {result['id']}")
                    self.log(f"  URL: https://www.youtube.com/watch?v={result['id']}")
                else:
                    failed += 1
                    self.log(f"✗ Failed to upload")
                    
            except Exception as e:
                failed += 1
                self.log(f"✗ Error: {e}")
            
            self.progress_bar['value'] = i
            self.root.update_idletasks()
        
        # Upload complete
        self.is_uploading = False
        self.progress_label.config(text=f"Complete! Uploaded: {uploaded}, Failed: {failed}")
        self.upload_button.config(state='normal', text="Start Upload", bg='#4CAF50')
        
        messagebox.showinfo(
            "Upload Complete",
            f"Upload finished!\n\n"
            f"Successful: {uploaded}\n"
            f"Failed: {failed}\n"
            f"Total: {total}"
        )
        
    def upload_video(self, video_path, title=None, description="", category="22", 
                    privacy="private", tags=None):
        """Upload a single video to YouTube"""
        if not self.youtube:
            raise Exception("Not authenticated")
        
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
            chunksize=-1,
            resumable=True
        )
        
        # Execute upload
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
                self.log(f"  Progress: {progress}%")
        
        return response


def main():
    root = Tk()
    app = YouTubeUploaderGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
