#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__' :
    year = int(input("Введите год"))
    a = year % 60

    if a >= 4 and a < 16:
        print("Зелено(й/го)")
    if a >= 16 and a < 28:
        print("Красно(й/го)")
    if a >= 28 and a < 40:
        print("Желто(й/го)")
    if a >= 40 and a < 52:
        print("Бело(й/го)")
    if a >= 52 and a < 4:
        print("Черно(й/го)")
    s = a % 12
    if s == 0:
        print("обезьяны")
    if s == 1:
        print("курицы")
    if s == 2:
        print("собаки")
    if s == 3:
        print("свиньи")
    if s == 4:
        print("мыши")
    if s == 5:
        print("коровы")
    if s == 6:
        print("тигра")
    if s == 7:
        print("зайца")
    if s == 8:
        print("дракона")
    if s == 9:
        print("змеи")
    if s == 10:
        print("лошади")
    if s == 11:
        print("овцы")
