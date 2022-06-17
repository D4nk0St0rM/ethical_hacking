#!/bin/bash


if [ $# -eq 0 ]; then
	echo "You need to specify an IP, for example: webenum.sh 10.0.0.10"
	exit 1
else
	IP=$1
fi

do_nikto() {
	echo "------------------------------------------------------------------------------"
	echo " Starting: nikto -host IP -port 80 >> nikto.txt"
	echo "------------------------------------------------------------------------------"
	echo "\n"

	nikto -host IP -port 80 >> nikto.out
}

do_dirb() {
	echo "------------------------------------------------------------------------------"
	echo " Starting: dirb http://$IP ./dirb_big.txt >> $DIRECTORY/dirb.txt"
	echo "------------------------------------------------------------------------------"
	echo "\n"
	
	dirb http://$IP ./dirb_big.txt >> dirb.out
	
}


