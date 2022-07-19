
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
> [hashcat](https://hashcat.net/wiki/doku.php?id=example_hashes)


#### Linux Passwd & Shadow
```
unshadow passwd.file shadow.file> unshadow.txt
john unshadow.txt --wordlist=/usr/share/wordlists/rockyou.txt
echo 'HASH' >> hashes.txt
hashcat -m 1800 -a 0 -o cracked.txt hashes.txt /usr/share/wordlists/rockyou.txt
```

#### Windows / Kerberoast

> hashcat
```
5500 | NetNTLMv1 / NetNTLMv1+ESS
27000 | NetNTLMv1 / NetNTLMv1+ESS (NT)
5600 | NetNTLMv2
27100 | NetNTLMv2 (NT)
1000 | NTLM
```

```
john --format=krb5tgs --wordlist=passwords_kerb.txt hashes.kerberoast

hashcat -m 13100 --force -a 0 hashes.kerberoast passwords_kerb.txt
./tgsrepcrack.py wordlist.txt 1-MSSQLSvc~sql01.medin.local~1433-MYDOMAIN.LOCAL.kirbi

```

#### Windows GPP from Groups.xml using gpp-decrypt

```
gpp-decrypt edBSHOwhZLTjt/QS9FeIcJ83mjWA98gw9guKOhJOdcqh+ZGMeXOsQbCpZ3xUjTLfCuNH8pG5aSVYdYw/NglVmQ
```
----

## General Hash Cracking

### Dictionary Attack

> Every word of a given list (a.k.a. dictionary) is hashed and compared against the target hash.

```powershell
hashcat --attack-mode 0 --hash-type $number $hashes_file $wordlist_file -r $my_rules
```

### Mask attack

Mask attack is an attack mode which optimize brute-force.

> Every possibility for a given character set and a given length (i.e. aaa, aab, aac, ...) is hashed and compared against the target hash.

```powershell
# Mask: upper*1+lower*5+digit*2 and upper*1+lower*6+digit*2
hashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 ?u?l?l?l?l?l?d?d
hashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 ?u?l?l?l?l?l?l?d?d
hashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 -1 "*+!??" ?u?l?l?l?l?l?d?d?1
hashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 -1 "*+!??" ?u?l?l?l?l?l?l?d?d?1

# Mask: upper*1+lower*3+digit*4 and upper*1+lower*3+digit*4
hashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 ?u?l?l?l?d?d?d?d
hashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 ?u?l?l?l?l?d?d?d?d
hashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 ?u?l?l?l?l?l?d?d?d?d
hashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 -1 "*+!??" ?u?l?l?l?d?d?d?d?1
hashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 -1 "*+!??" ?u?l?l?l?l?d?d?d?d?1

# Mask: lower*6 + digit*2 + special digit(+!?*)
hashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 -1 "*+!??" ?l?l?l?l?l?l?d?d?1
hashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 -1 "*+!??" ?l?l?l?l?l?l?d?d?1?1

# Mask: lower*6 + digit*2
hashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 /content/hashcat/masks/8char-1l-1u-1d-1s-compliant.hcmask
hashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 -1 ?l?d?u ?1?1?1?1?1?1?1?1

# Other examples
hashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 ?a?a?a?a?a?a?a?a?a
hashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 ?a?a?a?a?a?a?a?a
hashcat -m 1000 --status --status-timer 300 -w 4 -O /content/*.ntds -a 3 ?u?l?l?l?l?l?l?d?d?d?d
hashcat --attack-mode 3 --increment --increment-min 4 --increment-max 8 --hash-type $number $hashes_file "?a?a?a?a?a?a?a?a?a?a?a?a"
hashcat --attack-mode 3 --hash-type $number $hashes_file "?u?l?l?l?d?d?d?d?s"
hashcat --attack-mode 3 --hash-type $number $hashes_file "?a?a?a?a?a?a?a?a"
hashcat --attack-mode 3 --custom-charset1 "?u" --custom-charset2 "?l?u?d" --custom-charset3 "?d" --hash-type $number $hashes_file "?1?2?2?2?3"
```

| Shortcut  | Characters  |
|----|----------------------------|
| ?l | abcdefghijklmnopqrstuvwxyz |
| ?u | ABCDEFGHIJKLMNOPQRSTUVWXYZ |
| ?d | 0123456789 |
| ?s | !"#$%&'()*+,-./:;<=>?@[\]^_`{}~ |
| ?a | ?l?u?d?s |
| ?b | 0x00 - 0xff |


## John

```bash
# Run on password file containing hashes to be cracked
john passwd

# Use a specific wordlist
john --wordlist=<wordlist> passwd

# Use a specific wordlist with rules
john --wordlist=<wordlist> passwd --rules=Jumbo

# Show cracked passwords
john --show passwd

# Restore interrupted sessions
john --restore
```

## Rainbow tables

> The hash is looked for in a pre-computed table. It is a time-memory trade-off that allows cracking hashes faster, but costing a greater amount of memory than traditional brute-force of dictionary attacks. This attack cannot work if the hashed value is salted (i.e. hashed with an additional random value as prefix/suffix, making the pre-computed table irrelevant)

## Tips and Tricks

* Cloud GPU
    * [penglab - Abuse of Google Colab for cracking hashes. 🐧](https://github.com/mxrch/penglab)
    * [google-colab-hashcat - Google colab hash cracking](https://github.com/ShutdownRepo/google-colab-hashcat)
    * [Cloudtopolis - Zero Infrastructure Password Cracking](https://github.com/JoelGMSec/Cloudtopolis)
    * [Nephelees - also a NTDS cracking tool abusing Google Colab](https://github.com/swisskyrepo/Nephelees)
* Build a rig on premise
    * [Pentester's Portable Cracking Rig - $1000](https://www.netmux.com/blog/portable-cracking-rig)
    * [How To Build A Password Cracking Rig - 5000$](https://www.netmux.com/blog/how-to-build-a-password-cracking-rig)
* Online cracking
    * [Hashes.com](https://hashes.com/en/decrypt/hash)
    * [hashmob.net](https://hashmob.net/): great community with Discord
* Use the `loopback` in combination with rules and dictionary to keep cracking until you don't find new passsword: `hashcat --loopback --attack-mode 0 --rules-file $rules_file --hash-type $number $hashes_file $wordlist_file`