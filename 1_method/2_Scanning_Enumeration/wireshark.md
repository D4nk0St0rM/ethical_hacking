### Traffic Analysis - Wireshark

#### Configure Name Resolution
1.	Make a new profile
2.	Make a “hosts” file with format “ip hostname”
3.	Place that “hosts” file in the ~/.config/wireshark/configprofilename/  folder
4.	open pcap file, select your configuration profile, and ensure “view>>name resolution>>resolve network/transport address names” is checked

#### Configure Ports
1.	Go to “Edit>>preferences>>columns” and add src and dst ports to the display

#### Figuring out what multi-cast goes too
1.	Fill out “hosts” and “services” file if you can
2.	Click on various multi-cast products – generally the parameters will identify what the application is with a version or the company that made it.


#### Query for Common Ports
•	tcp.dstport >= 0 and tcp.dstport <= 10000 || tftp || dns

#### Saving off filters to make capture smaller
1.	Apply a filter
2.	Click “File>> Export Specified Packets” then save them to a file

#### Search for Strings
•	Edit >> find packet

#### Extracting files
•	file >> export objects

#### Find Hashes
•	net-creds.py file.pcap
