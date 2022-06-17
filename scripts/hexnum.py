#!bin/python3
# -*- coding: utf-8 -*-

import sys
import re


h = input("Enter hex value for conversion: ")
def main(h):
    dec = int(h, 16);
    print(h,"in Decimal =",str(dec));

main(h)
