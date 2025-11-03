# YouTube Video Uploader

A simple and efficient tool to automatically upload videos from one or multiple folders to YouTube.

## Features

- 🎥 Batch upload videos from multiple folders
- 🔐 OAuth2 authentication for secure YouTube account linking
- 📁 Support for recursive folder scanning
- 🎬 Support for multiple video formats (MP4, AVI, MOV, MKV, FLV, WMV, WebM, M4V, MPEG)
- 🔒 Configurable privacy settings (public, private, unlisted)
- 🏷️ Add custom descriptions, tags, and categories
- 📊 Upload progress tracking
- 💾 Persistent authentication (no need to re-authenticate every time)

## Prerequisites

Before using this application, you need to:

1. **Create a Google Cloud Project**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one

2. **Enable YouTube Data API v3**
   - In your project, navigate to "APIs & Services" > "Library"
   - Search for "YouTube Data API v3"
   - Click "Enable"

3. **Create OAuth 2.0 Credentials**
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth client ID"
   - Select "Desktop app" as the application type
   - Download the credentials JSON file
   - Rename it to `credentials.json` and place it in the same folder as the uploader

## Installation

### Using the Executable (Windows)

1. Download the latest release from the [Releases page](../../releases)
2. Extract the ZIP file
3. Place your `credentials.json` file in the same folder as the executable
4. Run `youtube_uploader.exe`

### Using Python (All Platforms)

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/youtube-video-uploader.git
   cd youtube-video-uploader
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place your `credentials.json` file in the project folder

## Usage

### Basic Usage

Upload videos from a single folder:
```bash
python youtube_uploader.py "C:\Videos\MyVideos"
```

Upload from multiple folders:
```bash
python youtube_uploader.py "C:\Videos\Folder1" "D:\More Videos"
```

### Advanced Options

**Recursive folder scanning:**
```bash
python youtube_uploader.py "C:\Videos" --recursive
```

**Set privacy status:**
```bash
python youtube_uploader.py "C:\Videos" --privacy public
```

**Add description and tags:**
```bash
python youtube_uploader.py "C:\Videos" --description "My awesome videos" --tags "tag1" "tag2" "tag3"
```

**Combine options:**
```bash
python youtube_uploader.py "C:\Videos" --recursive --privacy unlisted --description "Upload from batch"
```

### Command Line Options

- `folders`: One or more folder paths containing videos (required)
- `-r, --recursive`: Search subfolders recursively
- `-p, --privacy`: Privacy status - `public`, `private`, or `unlisted` (default: private)
- `-d, --description`: Description for uploaded videos
- `-c, --category`: YouTube category ID (default: 22 = People & Blogs)
- `-t, --tags`: Tags for uploaded videos
- `--credentials`: Path to credentials file (default: credentials.json)

### YouTube Category IDs

Common category IDs:
- 1: Film & Animation
- 10: Music
- 20: Gaming
- 22: People & Blogs (default)
- 23: Comedy
- 24: Entertainment
- 25: News & Politics
- 26: Howto & Style
- 27: Education
- 28: Science & Technology

## First-Time Setup

When you run the application for the first time:

1. The application will open a browser window
2. Sign in to your Google account
3. Grant the requested permissions
4. The application will save your credentials for future use

Your authentication token will be saved as `token.pickle` for subsequent uses.

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

## Security Notes

- Never commit or share your `credentials.json` or `token.pickle` files
- These files contain sensitive authentication information
- Keep them secure and private

## Troubleshooting

**"credentials.json not found" error:**
- Make sure you've downloaded the OAuth credentials from Google Cloud Console
- Ensure the file is named exactly `credentials.json`
- Place it in the same folder as the uploader

**Authentication issues:**
- Delete `token.pickle` and re-authenticate
- Verify that YouTube Data API v3 is enabled in your Google Cloud project

**Upload failures:**
- Check your internet connection
- Verify the video file is not corrupted
- Ensure you haven't exceeded YouTube's quota limits

## Quota Limits

YouTube API has daily quota limits:
- Default quota: 10,000 units per day
- Each video upload costs approximately 1600 units
- This allows roughly 6 uploads per day with the default quota
- You can request a quota increase from Google Cloud Console

## Building from Source

To create an executable:

```bash
pyinstaller --onefile --icon=youtube.ico youtube_uploader.py
```

The executable will be in the `dist` folder.

## License

MIT License - feel free to use and modify as needed.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This tool is for personal use. Make sure you comply with YouTube's Terms of Service and API usage policies.
