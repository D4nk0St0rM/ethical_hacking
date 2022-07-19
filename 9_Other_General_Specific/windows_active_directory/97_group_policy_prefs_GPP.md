### Group Policy Preferences (GPP)

- https://www.rapid7.com/blog/post/2016/07/27/pentesting-in-the-real-world-group-policy-pwnage/

Hunting GPP allowing admins to create policies with embedded credentials [patched in MS14-025] utilising attack against SMB

```
Machine\Policies\BLAHBLAHBLAH\Machine\preferences\Groups\groups.xml
# SVS_TGS
```

> metasploit check:
```
smb_enum_gpp
```
> Powersploit
```
python3/dist-packages/cme/data/powersploit/Exfiltration/Get-GPPAutologon.ps1
python3/dist-packages/cme/data/powersploit/Exfiltration/Get-GPPPassword.ps1
windows-resources/powersploit/Exfiltration/Get-GPPAutologon.ps1
windows-resources/powersploit/Exfiltration/Get-GPPPassword.ps1
```


> crack
```
gpp-decrypt <hash>
```
