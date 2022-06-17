#!/bin/bash

for name in $(cat subdomains.txt); do
	host $name.domain.com | grep "has address" | cut -d " " -f1,4
done
