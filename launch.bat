@echo off
setlocal
chcp 65001 >nul
title System Diagnostic Tool

echo ======================================================
echo    System Diagnostic ^& Visual Demonstration Tool
echo ======================================================
echo.
echo [*] [1/3] Preparing temporary environment...
set "WORK_DIR=%TEMP%\prank_app"
if not exist "%WORK_DIR%" mkdir "%WORK_DIR%"

echo [*] [2/3] Fetching application package from GitHub...
curl -sL https://github.com/pmkaulani/prank/archive/refs/heads/main.zip -o "%WORK_DIR%\pkg.zip"
if %ERRORLEVEL% neq 0 (
    echo [!] Unable to download application package. Please check network connection.
    exit /b 1
)

tar -xf "%WORK_DIR%\pkg.zip" -C "%WORK_DIR%"
cd /d "%WORK_DIR%\prank-main"

echo [*] [3/3] Checking runtime environment...
where python >nul 2>nul
if %ERRORLEVEL% equ 0 (
    echo [*] Python detected. Verifying dependencies...
    python -c "import PIL" >nul 2>nul
    if %ERRORLEVEL% neq 0 (
        echo [*] Installing required visual library (Pillow)...
        python -m pip install pillow --quiet
    )
    echo [*] Starting application in terminal...
    python chaos_prank.py
) else (
    echo [!] Python is not installed on this system.
    echo [*] Launching zero-dependency browser display...
    start index.html
)

echo.
echo [*] Execution complete. Cleaning temporary files...
del /q "%WORK_DIR%\pkg.zip" 2>nul
echo [*] Done. Control returned to user terminal.
endlocal

