@echo off
REM Build both CLI and GUI versions

echo ========================================
echo Building YouTube Video Uploader
echo Building BOTH CLI and GUI versions...
echo ========================================
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Failed to install dependencies!
    pause
    exit /b 1
)

echo.
echo Building CLI version...
pyinstaller --onefile --name youtube_uploader --console youtube_uploader.py
if errorlevel 1 (
    echo Failed to build CLI executable!
    pause
    exit /b 1
)

echo.
echo Building GUI version...
pyinstaller --onefile --windowed --name youtube_uploader_gui youtube_uploader_gui.py
if errorlevel 1 (
    echo Failed to build GUI executable!
    pause
    exit /b 1
)

echo.
echo ========================================
echo Build completed successfully!
echo CLI Executable: dist\youtube_uploader.exe
echo GUI Executable: dist\youtube_uploader_gui.exe
echo ========================================
echo.

pause
