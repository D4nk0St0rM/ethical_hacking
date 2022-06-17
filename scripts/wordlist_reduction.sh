#!/bin/bash

#temp file
tempFile="/tmp/"$RANDOM
extracFile="/tmp/"$RANDOM"-extrac"

# user choose
echo "Need to overwrite $tempFile and $extracFile"
echo "[ENTER] -> Contiune || [Ctrl]+C -> Stop"
read

files=`cat <<EOF
/usr/share/dict/wordlist-probable.txt
/usr/share/wfuzz/wordlist/general/megabeast.txt
/usr/share/sqlmap/data/txt/smalldict.txt
/usr/share/seclists/Miscellaneous/lang-english.txt
/usr/share/seclists/Miscellaneous/wordlist-skipfish.fuzz.txt
/usr/share/seclists/Discovery/DNS/dns-Jhaddix.txt
/usr/share/seclists/Discovery/Web-Content/common-and-french.txt
/usr/share/seclists/Discovery/Web-Content/big.txt
/usr/share/seclists/Discovery/Web-Content/raft-large-words.txt
/usr/share/seclists/Discovery/Web-Content/common.txt
/usr/share/seclists/Discovery/Web-Content/common-and-italian.txt
/usr/share/seclists/Discovery/Web-Content/common-and-spanish.txt
/usr/share/seclists/Discovery/Web-Content/common-and-portuguese.txt
/usr/share/seclists/Discovery/Web-Content/raft-large-words-lowercase.txt
/usr/share/seclists/Passwords/mssql-passwords-nansh0u-guardicore.txt
/usr/share/seclists/Passwords/bt4-password.txt
/usr/share/seclists/Passwords/Leaked-Databases/phpbb-cleaned-up.txt
/usr/share/seclists/Passwords/Leaked-Databases/phpbb.txt
/usr/share/seclists/Passwords/Software/cain-and-abel.txt
/usr/share/seclists/Passwords/dutch_common_wordlist.txt
/usr/share/seclists/Passwords/openwall.net-all.txt
/usr/share/seclists/Passwords/Honeypot-Captures/multiplesources-passwords-fabian-fingerle.de.txt
/usr/share/seclists/Passwords/darkc0de.txt
/usr/share/seclists/Usernames/xato-net-10-million-usernames.txt
/usr/share/seclists/Usernames/xato-net-10-million-usernames-dup.txt
/usr/share/wordlists/dirb/common.txt
/usr/share/wordlists/wfuzz/general/megabeast.txt
/usr/share/wordlists/rockyou.txt
EOF`

# extract
echo 'Extract /usr/share/dirb/wordlists/common.txt'
cp /usr/share/dirb/wordlists/common.txt $extracFile
for f in $files
do

        # Summarize -> $tempFile
        echo "Extract $f"
        cat $f $extracFile > $tempFile
        # Extract -> $extracFile
        sort $tempFile | uniq -d > $extracFile

done

rm $tempFile
echo "File $extracFile"