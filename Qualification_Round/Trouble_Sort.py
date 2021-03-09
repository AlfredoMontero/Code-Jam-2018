#!/usr/bin/env python
# coding: utf-8


def solve(lst,n):
    lst1 = lst[::2]
    lst2 = lst[1::2]
    lst1.sort()
    lst2.sort()
    if n%2 == 1:
        for i in range(n//2):
            if lst2[i] < lst1[i]:
                return 2*i
            elif lst2[i] > lst1[i+1]:
                return 2*i + 1
    else:
        for i in range(n//2 -1):
            if lst2[i] < lst1[i]:
                return 2*i
            elif lst2[i] > lst1[i+1]:
                return 2*i + 1
        if lst2[n//2 - 1] < lst1[n//2-1]:
            return n-2
    
    return "OK"

t = int(input())

for k in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    sol = solve(lst,n)
    print("Case #{}: {}".format(k+1, sol))

