@echo off
REM Build script for YouTube Video Uploader GUI

echo ========================================
echo Building YouTube Video Uploader GUI...
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
echo Building GUI executable with PyInstaller...
pyinstaller --onefile --windowed --name youtube_uploader_gui youtube_uploader_gui.py
if errorlevel 1 (
    echo Failed to build GUI executable!
    pause
    exit /b 1
)

echo.
echo ========================================
echo GUI Build completed successfully!
echo Executable location: dist\youtube_uploader_gui.exe
echo ========================================
echo.

pause
