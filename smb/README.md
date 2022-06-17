## smbclient + enum4linux + nmap

### pull files
```
smbclient '\\server\share' -N -c 'prompt OFF;recurse ON;cd 'path\to\directory\';lcd '~/path/to/download/to/';mget *'`

OR

smbclient '\\server\share'
mask ""
recurse ON
prompt OFF
cd 'path\to\remote\dir'
lcd '~/path/to/download/to/'
mget *
```


### List shares
```
smbclient -L <target-IP>
```

### List shares
```
smbclient -L \<target-IP\> -U username%password
```
### Connect
```
smbclient //\<target\>/\<share$\> -U username%password
``` 
### List files
```
smbclient //\<target\>/\<share$\> -c 'ls' password -U username
``` 
### List files
```
smbclient //\<target\>/\<share$\> -c 'cd folder; ls' password -U username
```
### Download a file
```
smbclient //\<target\>/\<share$\> -c 'cd folder;get desired_file_name' password -U username
```
### Copy a file
```
smbclient //\<target\>/\<share$\> -c 'put /var/www/my_local_file.txt .\target_folder\target_file.txt' password -U username
```
### Create a folder
```
smbclient //\<target\>/\<share$\> -c 'mkdir .\target_folder\new_folder' password -U username
```
### Rename a file
```
smbclient //\<target\>/\<share$\> -c 'rename current_file.txt new_file.txt' password -U username
```
### enum4linux anonymous session 
```
enum4linux -a \<target\>
```
### enum4linux authenticated session
```
enum4linux -a \<target\> -u \<user\> -p \<pass\>
```
### enum4linux Users
```
enum4linux -u \<user\> -p \<pass\> -U \<target\>
```
### enum4linux Group

```
enum4linux -u \<user\> -p \<pass\> -G \<target\>
```
### enum4linux Password policy
```
enum4linux -u \<user\> -p \<pass\> -P \<target\>
```
### nmap Users
```
nmap -p 445 --script smb-enum-users \<target\> --script-args smbuser=username,smbpass=password,smbdomain=domain
nmap -p 445 --script smb-enum-users \<target\> --script-args smbuser=username,smbhash=LM:NTLM,smbdomain=domain

nmap --script smb-enum-users.nse --script-args smbusername=User1,smbpass=Pass@1234,smbdomain=workstation -p445 192.168.1.10

nmap --script smb-enum-users.nse --script-args smbusername=User1,smbhash=aad3b435b51404eeaad3b435b51404ee:C318D62C8B3CA508DD753DDA8CC74028,smbdomain=mydomain -p445 192.168.1.10<br>
```
### nmap Groups
```
nmap -p 445 --script smb-enum-groups \<target\> --script-args smbuser=username,smbpass=password,smbdomain=domain
nmap -p 445 --script smb-enum-groups \<target\> --script-args smbuser=username,smbhash=LM:NTLM,smbdomain=domain
```
### nmap Shares
```
nmap -p 445 --script smb-enum-shares \<target\> --script-args smbuser=username,smbpass=password,smbdomain=domain
nmap -p 445 --script smb-enum-shares \<target\> --script-args smbuser=username,smbpass=LM:NTLM,smbdomain=domain
```
### nmap OS
```
nmap -p 445 --script smb-os-discovery \<target\>
```
### nmap Vuln Windows
```
nmap -p 445 --script smb-vuln-ms06-025 target-IP <br>
nmap -p 445 --script smb-vuln-ms07-029 target-IP <br>
nmap -p 445 --script smb-vuln-ms08-067 target-IP <br>
nmap -p 445 --script smb-vuln-ms10-054 target-IP <br>
nmap -p 445 --script smb-vuln-ms10-061 target-IP <br>
nmap -p 445 --script smb-vuln-ms17-010 target-IP <br>
```

### map Brute Force - WARNING account lock
```
nmap –p 445 --script smb-brute –script-args userdb=user-list.txt,passdb=pass-list.txt target-IP
```
