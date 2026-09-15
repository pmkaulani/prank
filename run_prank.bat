@echo off
chcp 65001 >nul
title System Diagnostic & Security Tool
color 0A
mode con: cols=100 lines=35
cls
where python >nul 2>nul
if %ERRORLEVEL% equ 0 (
    python chaos_prank.py
) else (
    echo [!] Python runtime not detected on this machine.
    echo [*] Launching standalone zero-dependency visual engine...
    timeout /t 1 >nul
    start index.html
)
pause
