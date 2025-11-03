# YouTube Video Uploader - Release v1.1.0

## 🎉 New Features

### Graphical User Interface (GUI)

**Major Update**: Added a full-featured graphical interface for easier use!

#### GUI Features:
- 🖥️ **User-Friendly Interface** - No command-line knowledge required
- 👁️ **Visual Authentication** - Clear authentication status indicator
- 📁 **Drag-and-Drop Folder Selection** - Easy folder management
- 📋 **Video Summary** - See all videos before uploading
- ⚙️ **Visual Settings** - Choose privacy, description, tags, and category from the interface
- 📊 **Real-Time Progress** - Watch upload progress with live updates
- 📝 **Detailed Logs** - See what's happening during upload
- ✅ **Upload Confirmation** - Review settings before starting

#### Privacy Settings (GUI):
- 🔒 **Private** - Videos only visible to you (default for safety)
- 🔓 **Unlisted** - Anyone with the link can view
- 🌐 **Public** - Visible to everyone on YouTube

#### Upload Information Fields:
- **Description** - Add a description for all videos
- **Tags** - Add comma-separated tags
- **Category** - Choose from 15 YouTube categories

### What's Included

**Two versions available:**
1. **youtube_uploader_gui.exe** - Graphical interface (recommended for beginners)
2. **youtube_uploader.exe** - Command-line version (for advanced users/automation)

### Installation

1. Download either or both executables from this release
2. Create a Google Cloud project and enable YouTube Data API v3
3. Download OAuth credentials as `credentials.json`
4. Place `credentials.json` in the same folder as the executable

**For GUI version:**
- Simply double-click `youtube_uploader_gui.exe` to launch

**For CLI version:**
- Run from command prompt: `youtube_uploader.exe "C:\Videos"`

### Screenshots

**GUI Main Window:**
- Authentication section with status indicator
- Folder selection with add/clear buttons
- Video list showing all files to be uploaded
- Privacy settings (Private/Unlisted/Public) with radio buttons
- Description, tags, and category fields
- Real-time progress bar and logs

### Usage Guide (GUI)

1. **Launch the application** - Double-click `youtube_uploader_gui.exe`
2. **Authenticate** - Click "Authenticate with YouTube" button
3. **Add folders** - Click "Add Folder" to select video folders
4. **Review videos** - Check the list of videos found
5. **Configure settings**:
   - Choose privacy: Private, Unlisted, or Public
   - Add description (optional)
   - Add tags (optional, comma-separated)
   - Select category
6. **Start upload** - Click "Start Upload" button
7. **Monitor progress** - Watch the progress bar and read the logs

### Requirements

- Windows 10 or later
- Google Cloud project with YouTube Data API v3 enabled
- OAuth 2.0 credentials (credentials.json)

### Technical Details

- **GUI Executable Size**: 27 MB
- **CLI Executable Size**: 24 MB
- Built with Python 3.10 and tkinter
- Standalone - no installation required

### What's New in v1.1.0

✨ **New:**
- Full graphical user interface (GUI)
- Visual privacy selection (Private/Unlisted/Public)
- Video summary before upload
- Real-time upload logs in the interface
- Upload confirmation dialog
- Build scripts for both CLI and GUI versions

🔧 **Improved:**
- Updated README with GUI instructions
- Better documentation for both versions

### Known Issues

- None reported

### Upgrade Notes

- Both CLI and GUI versions can coexist
- Both use the same `credentials.json` and `token.pickle`
- No need to re-authenticate when switching between versions

### Support

Having issues? Check the [README](https://github.com/youpaki/youtube-video-uploader) or open an issue on GitHub.

---

**Full Changelog**: https://github.com/youpaki/youtube-video-uploader/compare/v1.0.0...v1.1.0
