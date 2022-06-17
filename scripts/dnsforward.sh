#!/bin/bash


for name in $(cat subdomains.txt); do
	host $name.megacorpone.com | grep "has address" | cut -d " " -f1,4
done
