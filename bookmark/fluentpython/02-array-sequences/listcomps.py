# -*- coding: utf-8 -*-
import timeit

symbols = '$¢£¥€¤'
codes = []
print "origin codes are: ", codes
def cmp_list_comp():
    for symbol in symbols:
        codes.append(ord(symbol))
    #print "inited codes are: ", codes

total_time = timeit.timeit(cmp_list_comp)

listcomp_time = timeit.timeit('[ord(symbol) for symbol in "$¢£¥€¤"]')
print "listcomped time is: ", listcomp_time
print "no listcomp time is: ", total_time
