#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    set_s = set(s)
    char_freq={}
    temp =[]
    for i in set_s:
        count_char = s.count(i)
        if count_char not in temp:
            temp.append(count_char)
        if count_char not in char_freq.keys():
            char_freq[count_char]=[i]
        else:
            char_freq[count_char].append(i)
    temp.sort(reverse = True)
    counter = 0
    for j in temp:
        temp1 = char_freq[j]
        temp1.sort()
        for sym in temp1:
            print(sym+" "+str(j))
            counter+=1
            if counter == 3:
                exit()
        if counter == 3:
            exit()
        