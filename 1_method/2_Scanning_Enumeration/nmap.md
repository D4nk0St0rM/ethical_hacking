## Nmap
[source](https://github.com/jasonniebauer/Nmap-Cheatsheet)

| Technical Expertise | Usage |
|:--------------------|:------|
| Beginner            | [Zenmap](https://nmap.org/zenmap/) the graphical user interface for Nmap |
| Intermediate        | [Command line](https://nmap.org/) |
| Advanced            | Python scripting with the [Python-Nmap](https://pypi.org/project/python-nmap/) package |

## Basic Scanning Techniques
The `-s` switch determines the type of scan to perform.

| Nmap Switch | Description                 |
|:------------|:----------------------------|
| **-sA**     | ACK scan                    |
| **-sF**     | FIN scan                    |
| **-sI**     | IDLE scan                   |
| **-sL**     | DNS scan (a.k.a. list scan) |
| **-sN**     | NULL scan                   |
| **-sO**     | Protocol scan               |
| **-sP**     | Ping scan                   |
| **-sR**     | RPC scan                    |
| **-sS**     | SYN scan                    |
| **-sT**     | TCP connect scan            |
| **-sW**     | Windows scan                |
| **-sX**     | XMAS scan                   |

## Discovery Options
**Host Discovery**
The `-p` switch determines the type of ping to perform.

| Nmap Switch | Description                 |
|:------------|:----------------------------|
| **-PI**     | ICMP ping                   |
| **-Po**     | No ping                     |
| **-PS**     | SYN ping                    |
| **-PT**     | TCP ping                    |

## Service/Version Detection

| Nmap Switch | Description                  |
|:------------|:-----------------------------|
| **-sV**     | Enumerates software versions |

## Script Scan

| Nmap Switch | Description             |
|:------------|:------------------------|
| **-sC**     | Run all default scripts |

## Timing and Performance
The `-t` switch determines the speed and stealth performed.

| Nmap Switch | Description                 |
|:------------|:----------------------------|
| **-T0**     | Serial, slowest scan        |
| **-T1**     | Serial, slow scan           |
| **-T2**     | Serial, normal speed scan   |
| **-T3**     | Parallel, normal speed scan |
| **-T4**     | Parallel, fast scan         |

## Output Options

| Nmap Switch | Description   |
|:------------|:--------------|
| ``-oN``     | Normal output |
| ``-oX``     | XML output    |
| ``-oA``     | Normal, XML, and Grepable format all at once |


### Scan a Single Target
```bash
nmap $IP
```

### Scan Multiple Targets
```bash
nmap [target1, target2, etc]
```

### Scan a List of Targets
```bash
nmap -iL [list.txt]
```

### Scan a Range of Hosts
```bash
nmap [range of IP addresses]
```

### Scan an Entire Subnet
```bash
nmap [ip address/cdir]
```

### Scan Random Hosts
```bash
nmap -iR [number]
```

### Exclude Targets From a Scan
```bash
nmap [targets] --exclude [targets]
```

### Exclude Targets Using a List
```bash
nmap [targets] --excludefile [list.txt]
```

### Perform an Aggresive Scan
```bash
nmap -A $IP
```

### Scan an IPv6 Target
```bash
nmap -6 $IP
```

## Port Scanning Options

### Perform a Fast Scan
```bash
nmap -F $IP
```

### Scan Specific Ports
```bash
nmap -p [port(s)] $IP
```

### Scan Ports by Name
```bash
nmap -p [port name(s)] $IP
```

### Scan Ports by Protocol
```bash
nmap -sU -sT -p U:[ports],T:[ports] $IP
```

### Scan All Ports
```bash
nmap -p 1-65535 $IP
```

### Scan Top Ports
```bash
nmap --top-ports [number] $IP
```

### Perform a Sequential Port Scan
```bash
nmap -r $IP
```

### Attempt to Guess an Unknown OS
```bash
nmap -O --osscan-guess $IP
```

### Service Version Detection
```bash
nmap -sV $IP
```

### Troubleshoot Version Scan
```bash
nmap -sV --version-trace $IP
```

### Perform a RPC Scan
```bash
nmap -sR $IP
```

### Perform a Ping Only Scan
```bash
nmap -sn $IP
```

### Do Not Ping
```bash
nmap -Pn $IP
```

### TCP SYN Ping
```bash
nmap -PS $IP
```

### TCP ACK Ping
```bash
nmap -PA $IP
```

### UDP Ping
```bash
nmap -PU $IP
```

### SCTP INIT Ping
```bash
nmap -PY $IP
```

### ICMP Echo Ping
```bash
nmap -PE $IP
```
### ICMP Timestamp Ping
```bash
nmap -PP $IP
```

### ICMP Address Mask Ping
```bash
nmap -PM $IP
```

### IP Protocol Ping
```bash
nmap -PO $IP
```

### ARP ping
```bash
nmap -PR $IP
```

### Traceroute
```bash
nmap --traceroute $IP
```

### Force Reverse DNS Resolution
```bash
nmap -R $IP
```

### Disable Reverse DNS Resolution
```bash
nmap -n $IP
```

### Alternative DNS Lookup
```bash
nmap --system-dns $IP
```

### Manually Specify DNS Server
Can specify a single server or multiple.
```bash
nmap --dns-servers [servers] $IP
```

### Create a Host List
```bash
nmap -sL [targets]
```
## Firewall Evasion Techniques

### Fragment Packets
```bash
nmap -f $IP
```

### Specify a Specific MTU
```bash
nmap --mtu [MTU] $IP
```

### Use a Decoy
```bash
nmap -D RND:[number] $IP
```

### Idle Zombie Scan
```bash
nmap -sI [zombie] $IP
```

### Manually Specify a Source Port
```bash
nmap --source-port [port] $IP
```

### Append Random Data
```bash
nmap --data-length [size] $IP
```

### Randomize Target Scan Order
```bash
nmap --randomize-hosts $IP
```

### Spoof MAC Address
```bash
nmap --spoof-mac [MAC|0|vendor] $IP
```

### Send Bad Checksums
```bash
nmap --badsum $IP
```
  
## Advanced Scanning Functions

### TCP SYN Scan
```bash
nmap -sS $IP
```

### TCP Connect Scan
```
nmap -sT $IP
```

### UDP Scan
```bash
nmap -sU $IP
```

### TCP NULL Scan
```bash
nmap -sN $IP
```

### TCP FIN Scan
```bash
nmap -sF $IP
```

### Xmas Scan
```bash
nmap -sA $IP
```

### TCP ACK Scan
```bash
nmap -sA $IP
```

### Custom TCP Scan
```bash
nmap --scanflags [flags] $IP
```

### IP Protocol Scan
```bash
nmap -sO $IP
```

### Send Raw Ethernet Packets
```bash
nmap --send-eth $IP
```

### Send IP Packets
```bash
nmap --send-ip $IP
```

## Timing Options

### Timing Templates
```bash
nmap -T[0-5] $IP
```

### Set the Packet TTL
```bash
nmap --ttl [time] $IP
```

### Minimum NUmber of Parallel Operations
```bash
nmap --min-parallelism [number] $IP
```

### Maximum Number of Parallel Operations
```bash
nmap --max-parallelism [number] $IP
```

### Minimum Host Group Size
```bash
nmap --min-hostgroup [number] [targets]
```

### Maximum Host Group Size
```bash
nmap --max-hostgroup [number] [targets]
```

### Maximum RTT Timeout
```bash
nmap --initial-rtt-timeout [time] $IP
```

### Initial RTT Timeout
```bash
nmap --max-rtt-timeout [TTL] $IP
```

### Maximum Number of Retries
```bash
nmap --max-retries [number] $IP
```

### Host Timeout
```bash
nmap --host-timeout [time] $IP
```

### Minimum Scan Delay
```bash
nmap --scan-delay [time] $IP
```

### Maxmimum Scan Delay
```bash
nmap --max-scan-delay [time] $IP
```

### Minimum Packet Rate
```bash
nmap --min-rate [number] $IP
```

### Maximum Packet Rate
```bash
nmap --max-rate [number] $IP
```

### Defeat Reset Rate Limits
```bash
nmap --defeat-rst-ratelimit $IP
```



### Save Output to a Text File
```bash
nmap -oN [scan.txt] $IP
```

### Save Output to a XML File
```bash
nmap -oX [scan.xml] $IP
```

### Grepable Output
```bash
nmap -oG [scan.txt] $IP
```

### Output All Supported File Types
```bash
nmap -oA [path/filename] $IP
```

### Periodically Display Statistics
```bash
nmap --stats-every [time] $IP
```

### 1337 Output
```bash
nmap -oS [scan.txt] $IP
```

## Compare Scans

### Comparison Using Ndiff
```bash
ndiff [scan1.xml] [scan2.xml]
```

### Ndiff Verbose Mode
```bash
ndiff -v [scan1.xml] [scan2.xml]
```

### XML Output Mode
```bash
ndiff --xml [scan1.xml] [scan2.xml]
```

## Troubleshooting and Debugging

### Get Help
```bash
nmap -h
```

### Display Nmap Version
```bash
nmap -V
```

### Verbose Output
```bash
nmap -v $IP
```

### Debugging
```bash
nmap -d $IP
```

### Display Port State Reason
```bash
nmap --reason $IP
```

### Only Display Open Ports
```bash
nmap --open $IP
```

### Trace Packets
```bash
nmap --packet-trace $IP
```

### Display Host Networking
```bash
nmap --iflist
```

### Specify a Network Interface
```bash
nmap -e [interface] $IP
```

## Nmap Scripting Engine

### Execute Individual Scripts
```bash
nmap --script [script.nse] $IP
```

### Execute Multiple Scripts
```bash
nmap --script [expression] $IP
```

### Execute Scripts by Category
```bash
nmap --script [category] $IP
```

### Execute Multiple Script Categories
```bash
nmap --script [category1,category2,etc]
```

### Troubleshoot Scripts
```bash
nmap --script [script] --script-trace $IP
```

### Update the Script Database
```bash
nmap --script-updatedb
```


**Reference Sites**
- [X] [Nmap - The Basics](https://www.youtube.com/watch?v=_JvtO-oe8k8)  
- [ ] [Reference link 1](https://hackertarget.com/nmap-cheatsheet-a-quick-reference-guide/)  
- [ ] [Beginner's Guide to Nmap](https://www.linux.com/learn/beginners-guide-nmap)  
- [ ] [Top 32 Nmap Command](https://www.cyberciti.biz/security/nmap-command-examples-tutorials/)  
- [ ] [Nmap Linux man page](https://linux.die.net/man/1/nmap)  
- [ ] [29 Practical Examples of Nmap Commands](https://www.tecmint.com/nmap-command-examples/)  
- [ ] [Nmap Scanning Types, Scanning Commands , NSE Scripts](https://medium.com/@infosecsanyam/nmap-cheat-sheet-nmap-scanning-types-scanning-commands-nse-scripts-868a7bd7f692)  
- [ ] [Nmap CheatSheet](https://www.cheatography.com/netwrkspider/cheat-sheets/nmap-cheatsheet/)  
- [ ] [Nmap Cheat Sheet](https://highon.coffee/blog/nmap-cheat-sheet/)  
- [ ] [Nmap Cheat Sheet: From Discovery to Exploits](https://resources.infosecinstitute.com/nmap-cheat-sheet/)  
- [ ] [Nmap: my own cheatsheet](https://www.andreafortuna.org/2018/03/12/nmap-my-own-cheatsheet/)  
- [ ] [NMAP Commands Cheatsheet](https://hackersonlineclub.com/nmap-commands-cheatsheet/)  
- [ ] [Nmap Cheat Sheet](https://www.stationx.net/nmap-cheat-sheet/)  
- [ ] [Nmap Cheat Sheet](http://nmapcookbook.blogspot.com/2010/02/nmap-cheat-sheet.html)  