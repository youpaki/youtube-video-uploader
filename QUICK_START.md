# Quick Start Guide - YouTube Video Uploader

## Before You Start

You need to set up YouTube API credentials to use this application.

### Step 1: Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click "Create Project" or select existing project
3. Give your project a name (e.g., "YouTube Uploader")

### Step 2: Enable YouTube Data API v3

1. In the left sidebar, go to "APIs & Services" > "Library"
2. Search for "YouTube Data API v3"
3. Click on it and press "Enable"

### Step 3: Create OAuth Credentials

1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth client ID"
3. If prompted, configure the OAuth consent screen:
   - Choose "External" user type
   - Fill in the required fields (app name, email)
   - Add your email as a test user
   - Save and continue through all steps
4. Back in Credentials, create "OAuth client ID"
5. Choose "Desktop app" as application type
6. Download the JSON file
7. Rename it to `credentials.json`

### Step 4: Run the Application

1. Download the latest release from: https://github.com/youpaki/youtube-video-uploader/releases
2. Extract the ZIP file
3. Place `credentials.json` in the same folder as `youtube_uploader.exe`
4. Open Command Prompt or PowerShell in that folder
5. Run the command (example):
   ```
   youtube_uploader.exe "C:\Your\Videos\Folder"
   ```

### Step 5: First Authentication

1. A browser window will open automatically
2. Sign in with your Google account
3. Click "Allow" to grant permissions
4. The browser will show "The authentication flow has completed"
5. Close the browser and return to the application
6. Your credentials are saved - you won't need to do this again!

## Common Commands

**Upload from one folder:**
```
youtube_uploader.exe "C:\Videos"
```

**Upload from multiple folders:**
```
youtube_uploader.exe "C:\Videos\Folder1" "C:\Videos\Folder2"
```

**Search subfolders (recursive):**
```
youtube_uploader.exe "C:\Videos" --recursive
```

**Upload as public:**
```
youtube_uploader.exe "C:\Videos" --privacy public
```

**Upload as unlisted:**
```
youtube_uploader.exe "C:\Videos" --privacy unlisted
```

**Add description:**
```
youtube_uploader.exe "C:\Videos" --description "My video collection"
```

**Add tags:**
```
youtube_uploader.exe "C:\Videos" --tags "gaming" "tutorial" "2025"
```

**Combine options:**
```
youtube_uploader.exe "C:\Videos" --recursive --privacy unlisted --description "Personal videos" --tags "family" "memories"
```

**Get help:**
```
youtube_uploader.exe --help
```

## Supported Video Formats

- MP4
- AVI
- MOV
- MKV
- FLV
- WMV
- WebM
- M4V
- MPEG/MPG

## Troubleshooting

**"credentials.json not found"**
- Make sure the file is in the same folder as the .exe
- Check the filename is exactly `credentials.json` (case-sensitive)

**Authentication fails**
- Delete `token.pickle` if it exists
- Run the application again to re-authenticate

**Upload fails**
- Check your internet connection
- Verify the video file isn't corrupted
- Check YouTube API quota (default: ~6 uploads/day)

**Quota exceeded**
- Wait 24 hours for quota to reset
- Or request quota increase in Google Cloud Console

## Important Notes

- Default privacy is "private" for safety
- Videos upload to your account, not a channel (unless you specify)
- Keep `credentials.json` and `token.pickle` secure
- Never share these files with anyone
- Each upload costs ~1600 quota units
- Default quota is 10,000 units per day

## Need Help?

Visit the GitHub repository: https://github.com/youpaki/youtube-video-uploader
