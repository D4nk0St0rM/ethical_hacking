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



#### Bloodhound




##### Invoke-Bloodhound




## Attacks








