#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
if __name__ == '__main__':
    n= int (input("Введите номер месяца"))
    if n == 1 or n ==3 or n ==5 or n ==7 or n==8 or n==10 or n==12 :
        print("31 day")
    elif n == 2 :
        print("28 or 29 days")
    elif n==9 or n==4 or n == 6 or n==9 or n==11 :
        print("30 days")
    else:
        print("Error!", file =sys.stderr)
        exit (1)