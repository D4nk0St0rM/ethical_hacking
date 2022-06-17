
### Password / Hash Cracking

#### Identification of Hash Type

> [hashID](https://github.com/psypanda/hashID)
```
$ pip install hashid
$ pip install --upgrade hashid
$ pip uninstall hashid
```
> [NameThatHash](https://github.com/HashPals/Name-That-Hash)
```
$ pip3 install name-that-hash
$ pip install name-that-hash
```

#### Linux Passwd & Shadow
```
unshadow passwd.file shadow.file> unshadow.txt
john unshadow.txt --wordlist=/usr/share/wordlists/rockyou.txt
echo 'HASH' >> hashes.txt
hashcat -m 1800 -a 0 -o cracked.txt hashes.txt /usr/share/wordlists/rockyou.txt
```

#### Windows / Kerberoast
```
john --format=krb5tgs --wordlist=passwords_kerb.txt hashes.kerberoast
hashcat -m 13100 --force -a 0 hashes.kerberoast passwords_kerb.txt
./tgsrepcrack.py wordlist.txt 1-MSSQLSvc~sql01.medin.local~1433-MYDOMAIN.LOCAL.kirbi
```

#### Windows GPP from Groups.xml using gpp-decrypt

```
gpp-decrypt edBSHOwhZLTjt/QS9FeIcJ83mjWA98gw9guKOhJOdcqh+ZGMeXOsQbCpZ3xUjTLfCuNH8pG5aSVYdYw/NglVmQ
```

