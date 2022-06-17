#!/bin/python

import socket
import sys
import time
import re

ips = [
"192.168.1.22",
"192.168.1.72"
]

users = ["root"]

userfile = open("/fileWithUsernames.txt", "r")
for line in userfile:
    user = line.strip("\n")
    users.append(user)


for ip in ips:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 25))
    banner = s.recv(1024)

    print "****************************"
    print "Report for " + ip
    print banner
    s.send('VRFY root \r\n')
    answerUsername = s.recv(1024)
    answerAsArray = answerUsername.split(" ")

    if answerAsArray[0] == "502":
        print "VRFY failed"
    if answerAsArray[0] == "250":
        print "VRFY command succeeded.\nProceeding to test usernames"

        for username in users:
            time.sleep(5)
            s.send("VRFY " + username + "\r\n")

            answerUsername = s.recv(1024)
            answerUsernameArray = answerUsername.split(" ")
            print answerUsernameArray[0]
            if answerUsernameArray[0] == "250":
                print "Exists: " + username.strip("\n") 
            else :
                print "Does NOT exist: " + username.strip("\n")
    if answerAsArray[0] == "252":
        print "FAILED - Cannot verify user"
    else:
        "Some other error or whatever here it is: \n" + answerUsername



    s.close()
