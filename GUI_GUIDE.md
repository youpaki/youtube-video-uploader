# GUI Quick Guide - YouTube Video Uploader

## 🖥️ Graphical User Interface

The GUI version provides an easy-to-use interface for uploading videos to YouTube.

### Main Window Sections

#### 1. Authentication Section
- **Status Indicator**: Shows if you're authenticated (red = not authenticated, green = authenticated)
- **Authenticate Button**: Click to link your YouTube account
  - Browser window will open
  - Sign in with Google
  - Grant permissions
  - Done! You're authenticated

#### 2. Video Folders Section
- **Add Folder Button**: Click to select a folder containing videos
- **Clear All Button**: Remove all selected folders
- **Recursive Checkbox**: Check to search subfolders
- **Folder List**: Shows all selected folders

#### 3. Videos to Upload Section
- **Video Count**: Shows how many videos were found
- **Video List**: Displays the name of each video that will be uploaded
- Automatically updates when you add folders or toggle recursive search

#### 4. Upload Settings Section

**Privacy (Required - Choose one):**
- ⚫ **Private** (Default, Recommended)
  - Only you can see the videos
  - Safest option
  - You can change to public later on YouTube
  
- ⚫ **Unlisted**
  - Anyone with the link can view
  - Not shown in search results
  - Good for sharing privately
  
- ⚫ **Public**
  - Everyone can see your videos
  - Shown in search results and on your channel
  - Use with caution

**Description (Optional):**
- Text that appears below your videos
- Will be applied to ALL uploaded videos
- Example: "Home videos from 2025"

**Tags (Optional):**
- Comma-separated keywords
- Helps people find your videos
- Example: "family, vacation, 2025"

**Category (Required):**
- Dropdown menu with 15 YouTube categories
- Default: "People & Blogs"
- Choose the category that best fits your videos

#### 5. Progress Section
- **Progress Label**: Shows current status (Ready, Uploading, Complete)
- **Progress Bar**: Visual indicator of upload progress
- **Log Area**: Detailed information about each upload
  - Shows which video is being uploaded
  - Upload progress percentage
  - Success/failure status
  - Video URLs after upload

#### 6. Start Upload Button
- Large green button at the bottom
- Click to begin uploading
- Will ask for confirmation before starting
- Shows: "Upload X video(s) as 'privacy'?"
- Button becomes disabled during upload

### Step-by-Step Workflow

1. **Launch** the application
   ```
   Double-click youtube_uploader_gui.exe
   ```

2. **Authenticate** (first time only)
   - Click "Authenticate with YouTube"
   - Sign in when browser opens
   - Close browser when done
   - Status turns green ✓

3. **Add videos**
   - Click "Add Folder"
   - Select folder(s) with videos
   - Check "recursive" if needed
   - See video count update

4. **Review**
   - Check the video list
   - Verify count is correct
   - Make sure you want to upload these

5. **Configure**
   - Choose privacy setting
   - Add description (optional)
   - Add tags (optional)
   - Select category

6. **Upload**
   - Click "Start Upload"
   - Click "Yes" to confirm
   - Watch progress in real-time
   - Wait for completion message

7. **Done!**
   - Videos are now on YouTube
   - Check the log for video URLs
   - Visit YouTube to see your videos

### Tips & Tricks

**Safety First:**
- Always use "Private" when testing
- Review the video list before uploading
- Confirm the count matches your expectations

**Efficiency:**
- Add multiple folders at once
- Use recursive for nested folders
- Set all options before starting upload

**Troubleshooting:**
- Red authentication? Click authenticate again
- No videos found? Check folder path
- Upload failed? Check log for details

**Reusing:**
- Authentication persists (token.pickle saved)
- No need to re-authenticate next time
- Same credentials for CLI and GUI versions

### Keyboard Shortcuts

- None currently (mouse/touch only)

### Window Controls

- **Minimize**: Use Windows minimize button
- **Resize**: Drag window edges (minimum 900x700)
- **Close**: Click X or complete upload first

### Error Messages

**"credentials.json not found"**
- Solution: Place credentials.json in same folder as .exe

**"Please authenticate first!"**
- Solution: Click "Authenticate with YouTube" button

**"No videos to upload!"**
- Solution: Add at least one folder with videos

**"Upload already in progress!"**
- Solution: Wait for current upload to finish

### Privacy Explanation

| Setting | Visibility | Search | Share Link | Recommended For |
|---------|-----------|--------|------------|-----------------|
| Private | Only you | No | No | Testing, Personal |
| Unlisted | Anyone with link | No | Yes | Friends, Family |
| Public | Everyone | Yes | Yes | Public content |

### YouTube Category IDs

The dropdown shows these categories:
- Film & Animation
- Autos & Vehicles
- Music
- Pets & Animals
- Sports
- Travel & Events
- Gaming
- People & Blogs (Default)
- Comedy
- Entertainment
- News & Politics
- Howto & Style
- Education
- Science & Technology
- Nonprofits & Activism

### File Formats Supported

The GUI will find and upload these video formats:
- MP4
- AVI
- MOV
- MKV
- FLV
- WMV
- WebM
- M4V
- MPEG
- MPG

### Performance Notes

- Each upload takes time (depends on file size)
- Progress bar shows overall progress
- Log shows per-video progress
- Don't close window during upload
- Internet speed affects upload time

### Quota Limits

- YouTube API has daily limits
- Default: ~6 video uploads per day
- Each upload costs ~1,600 quota units
- Quota resets at midnight Pacific Time
- Request increase from Google Cloud Console

### After Upload

- Videos appear on your YouTube channel
- Check "My videos" on YouTube
- Edit video details anytime
- Change privacy settings later
- Add custom thumbnails on YouTube

### Need More Help?

- Check the main README: https://github.com/youpaki/youtube-video-uploader
- Report issues on GitHub
- See QUICK_START.md for OAuth setup
- Review PROJECT_SUMMARY.md for technical details

---

**Enjoy uploading your videos!** 🎥✨
