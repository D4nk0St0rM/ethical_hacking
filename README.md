[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Press+Start&size=30&duration=4000&color=1E0DC6EE&center=true&vCenter=true&multiline=true&width=1200&height=150&lines=D4nk0St0rM;SpReAd+L0vE+%26+ShArE+Kn0wLeDgE;%60I'm+smart+enough+to+know+that+I'm+dumb%60)](https://git.io/typing-svg)

____

<p align="center">
    <img src="assets/sun_tzu.jpeg">

___

#### List of applications for installation that are helpful / required for some tools
[for i in $(cat list); do sudo apt install $i -y; done](https://raw.githubusercontent.com/D4nk0St0rM/kali_instance_setup/main/app-install.list)

___

# Method
## Reconnaissance and scanning / Enumeration are the most important step

- Client Risk analysis
    - Consider specific risk level for areas of client concern
    - design pentest based on client risk areas
- Intel gathering / Perform Reconnaissance
- [Scanning and Enumeration](https://book.hacktricks.xyz/generic-methodologies-and-resources/pentesting-network)
    - nmap scan — review findings
    - [Port 80/443](https://book.hacktricks.xyz/network-services-pentesting/pentesting-web) or [Web App Pentesting](https://www.youtube.com/watch?v=azYwfI26oXo&t=556s)
        - /etc/hosts
        — run Nikto
        - run FFuF or sublist3r
        - [Broken Access Control](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)
        - source code
        - Cross Site Scripting ([XSS](https://owasp.org/www-community/attacks/xss/))
        - SQL Injection
    - review the other open ports/services for potential initial attack vectors
        - [Port 21](https://book.hacktricks.xyz/network-services-pentesting/pentesting-ftp) (FTP) login anonymously and download or upload files
        - [Port 22](https://book.hacktricks.xyz/network-services-pentesting/pentesting-ssh) (SSH) brute force the credentials and login
        - [Port 5985](https://book.hacktricks.xyz/network-services-pentesting/5985-5986-pentesting-winrm) (Windows Remote Management (WinRM) any credentials to use EvilWinRM or [crackmapexec](https://www.ivoidwarranties.tech/posts/pentesting-tuts/cme/crackmapexec-cheatsheet/)
- Gaining access / Exploitation
    - Escalation of privilege
        - [Windows](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation)
        - Linux(https://book.hacktricks.xyz/linux-hardening/linux-privilege-escalation-checklist)
        - search every directory and cat or type ```*.txt``` files
        - find next attack vector
            - additional users
            - running processes
            - cron jobs
            - out of date software
            - kernel exploits
            - WinPEAS/ LinPEAS
            - dump credentials, hashes, or tickets with Mimikatz
- Maintain access
- Cover tracks and insert backdoors


### To remember

- document and screenshot

## Summary of Standard Toolset

- BloodHound: Displays visual of AD environment
- CrackMapExec: Do Some Research
- Impacket: Great for abusing Windows Network Protocols
- LinPEAS: Displays Lin Priv Esc Vectors
- WinPEAS: Displays Windows Priv Esc Vectors
- PowerView: Allows for enumeration of an AD environment
- PowerUp: Displays Windows Priv Esc Vectors based on system misconfigs
- Mimikatz: Credential Stealer
- Chisel/SSHuttle: Port Forwarding (pivoting)
- hashcat / John : Cracking hashes
