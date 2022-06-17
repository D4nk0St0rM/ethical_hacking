#!/usr/bin/python

import ipaddress
import os


#ip address string must be in unicode to use ipaddress module
network = ipaddress.ip_network(unicode("10.11.1.0/24"))

print("Running Python ping sweep of target IP range 10.11.1.0/24")

for i in network.hosts():
	#str(i)
	
	response = os.system("ping %s -c 1 > /dev/null" %i)
	
        if response == 0:
                print("%s UP" %i)
        else:
                print("%s No response" %i)

print("Ping sweep complete")


#Import os module
import os

# Ask the user to enter string to search
search_path = input("Enter directory path to search : ")
file_type = input("File Type : ")
search_str = input("Enter the search string : ")

# Append a directory separator if not already present
if not (search_path.endswith("/") or search_path.endswith("\\") ): 
        search_path = search_path + "/"
                                                          
# If path does not exist, set search path to current directory
if not os.path.exists(search_path):
        search_path ="."

# Repeat for each file in the directory  
for fname in os.listdir(path=search_path):

   # Apply file type filter   
   if fname.endswith(file_type):

        # Open file for reading
        fo = open(search_path + fname)

        # Read the first line from the file
        line = fo.readline()

        # Initialize counter for line number
        line_no = 1

        # Loop until EOF
        while line != '' :
                # Search for string in line
                index = line.find(search_str)
                if ( index != -1) :
                    print(fname, "[", line_no, ",", index, "] ", line, sep="")

                # Read next line
                line = fo.readline()  

                # Increment line counter
                line_no += 1
        # Close the files
        fo.close()