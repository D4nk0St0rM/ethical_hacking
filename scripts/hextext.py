#!/bin/python3
# -*- coding: utf-8 -*-

def hextext(n):
    print(bytearray.fromhex(n).decode())

n = input("Enter the hexadecimal value for conversion to text value: ")

hextext(n)
