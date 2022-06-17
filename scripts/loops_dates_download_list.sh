#!/bin/bash


d="2020-01-01" && until [[ $d > 2022-01-01 ]]; do  echo "$d"; d=$(date -I -d "$d + 1 day"); done > date
for i in $(cat dates); do wget -P 20 "http://$(cat ip)/Documents/$i-upload.pdf" ; done




