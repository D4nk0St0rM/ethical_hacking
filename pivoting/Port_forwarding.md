#### rinetd

> Outbound traffic filtering bypass
```bash
sudo apt update && sudo apt install rinetd
# local port to  outside port
0.0.0.0 80 220.60.200.100 80
sudo service rinetd restart



