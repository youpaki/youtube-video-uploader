# YouTube Video Uploader - Release v1.0.0

## What's New

🎉 **Initial Release** - Automatic YouTube Video Uploader

### Features

- 🎥 **Batch Upload Videos** - Upload multiple videos from one or more folders
- 🔐 **Secure Authentication** - OAuth2 authentication to link your YouTube account
- 📁 **Flexible File Selection** - Support for recursive folder scanning
- 🎬 **Multiple Formats** - MP4, AVI, MOV, MKV, FLV, WMV, WebM, M4V, MPEG
- 🔒 **Privacy Controls** - Set videos as public, private, or unlisted
- 🏷️ **Customization** - Add descriptions, tags, and categories
- 📊 **Progress Tracking** - Real-time upload progress display
- 💾 **Persistent Login** - Stay authenticated between sessions

### Installation

1. Download `youtube_uploader.exe` from this release
2. Create a Google Cloud project and enable YouTube Data API v3
3. Download OAuth credentials as `credentials.json`
4. Place both files in the same folder
5. Run the executable

### Usage Examples

**Upload from a single folder:**
```
youtube_uploader.exe "C:\Videos\MyVideos"
```

**Upload from multiple folders:**
```
youtube_uploader.exe "C:\Videos\Folder1" "D:\More Videos"
```

**Upload recursively with custom privacy:**
```
youtube_uploader.exe "C:\Videos" --recursive --privacy public
```

**Full help:**
```
youtube_uploader.exe --help
```

### Requirements

- Windows 10 or later
- Google Cloud project with YouTube Data API v3 enabled
- OAuth 2.0 credentials (credentials.json)

### Setup Guide

For detailed setup instructions, please see the [README](https://github.com/youpaki/youtube-video-uploader/blob/master/README.md).

### Notes

- Default privacy status is "private" for safety
- Videos can be made public after upload
- Daily upload quota: ~6 videos with default API quota
- Request quota increase from Google Cloud Console if needed

### Support

Having issues? Check the [README](https://github.com/youpaki/youtube-video-uploader) or open an issue on GitHub.

---

**Full Changelog**: https://github.com/youpaki/youtube-video-uploader/commits/v1.0.0
