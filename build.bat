@echo off
REM Build script for YouTube Video Uploader

echo ========================================
echo Building YouTube Video Uploader...
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
echo Building executable with PyInstaller...
pyinstaller --onefile --name youtube_uploader --console youtube_uploader.py
if errorlevel 1 (
    echo Failed to build executable!
    pause
    exit /b 1
)

echo.
echo ========================================
echo Build completed successfully!
echo Executable location: dist\youtube_uploader.exe
echo ========================================
echo.

pause
