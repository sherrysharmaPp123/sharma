#!/bin/bash

SITE="$1"
PORT=8080

if [ -z "$SITE" ]; then
  echo "[-] No template selected. Usage: ./start_server.sh <site_folder>"
  exit 1
fi

SITE_PATH="sites/$SITE"

if [ ! -d "$SITE_PATH" ]; then
  echo "[-] Folder $SITE_PATH does not exist."
  exit 1
fi

echo "[+] Starting PHP server on http://127.0.0.1:$PORT with $SITE_PATH"
php -S 127.0.0.1:$PORT -t $SITE_PATH > .server_log.txt 2>&1 &

sleep 3

if ! pgrep -f "php -S 127.0.0.1:$PORT" > /dev/null; then
  echo "[-] PHP server failed to start. Check .server_log.txt"
  exit 1
fi

echo "[✓] PHP server is running."
echo "[+] Starting Cloudflare tunnel..."
cloudflared tunnel --url http://127.0.0.1:$PORT --no-autoupdate

