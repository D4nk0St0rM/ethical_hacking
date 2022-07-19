#### Show me all URGENT (URG) packets...
```bash
tcpdump 'tcp[13] & 32 != 0'
```
#### Show me all ACKNOWLEDGE (ACK) packets...
```bash
tcpdump 'tcp[13] & 16 != 0'
```
#### Show me all PUSH (PSH) packets...
```bash
tcpdump 'tcp[13] & 8 != 0'
```
#### Show me all RESET (RST) packets...
```bash
tcpdump 'tcp[13] & 4 != 0'
```
#### Show me all SYNCHRONIZE (SYN) packets...
```bash
tcpdump 'tcp[13] & 2 != 0'
```
#### Show me all FINISH (FIN) packets...
```bash
tcpdump 'tcp[13] & 1 != 0'
```
#### Show me all SYNCHRONIZE/ACKNOWLEDGE (SYNACK) packets...
```bash
tcpdump 'tcp[13] = 18'
```