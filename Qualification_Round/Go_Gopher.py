#!/usr/bin/env python
# coding: utf-8

def check_values(j,values):
    for i in range(1,4):
        for k in range(-1,2):
            if (i,j+k) not in values:
                return True
    return False

def solve(a):
        values = []
        i = 2
        j = 2
        while True:
            while check_values(j,values):
                print(i,j , flush = True)
                val = tuple(map(int, input().split()))
                values.append(val)
                if val == (0,0):
                    return
            else:
                j += 3
    

t = int(input())

for _ in range(t):
    a = int(input())
    solve(a)

