#!/usr/bin/env python
# coding: utf-8

def is_impossible(d,p):
    if p.count("S") > d:
        return True
    else:
        return False

def calculate_damage(p):
    plst = list(p)
    damage = 0
    multiplier = 1
    for i in reversed(plst):
        if i == "C":
            multiplier *= 2
        else:
            damage += multiplier
    return damage

def solve(d,p):
    p = "".join(reversed(p))
    count = 0
    while calculate_damage(p) > d:
        p = list(p)
        s_index = p.index("S")
        c_index = p.index("C",s_index)
        p[c_index] = "S"
        p[c_index-1] = "C"
        p = ''.join(p)
        count += 1
    return count

t = int(input())

for i in range(t):
    d , p = input().split()
    d = int(d)
    if is_impossible(d,p):
        sol = "IMPOSSIBLE"
    else:
        sol = solve(d,p)
    print("Case #{}: {}".format(i+1, sol))

