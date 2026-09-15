# PowerShell Launcher for Real Terminal Chaos Prank (Instant Launch)
$Host.UI.RawUI.WindowTitle = "System Diagnostic & Security Tool"
[Console]::ForegroundColor = [ConsoleColor]::Green
Clear-Host

if (Get-Command python -ErrorAction SilentlyContinue) {
    python chaos_prank.py
} else {
    Write-Host "[!] Python runtime not detected on this machine." -ForegroundColor Yellow
    Write-Host "[*] Launching standalone zero-dependency visual engine..." -ForegroundColor Cyan
    Start-Sleep -Seconds 1
    Start-Process "index.html"
}
