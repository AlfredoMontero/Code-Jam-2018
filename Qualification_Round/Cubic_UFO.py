#!/usr/bin/env python
# coding: utf-8

import math

def area(theta):
    ar = math.sqrt(2)  * (math.sin(theta) + math.sqrt(2) / 2 * math.cos(theta))
    return ar

def get_angle(a):
    theta0 = 0
    theta1 = math.pi/4+0.17 + 0.001
    while True:
        theta = (theta0 + theta1) / 2
        ar = area(theta)
        if abs(ar-a) < 0.000001:
            return theta
        elif a > ar:
            theta0 = theta
        else:
            theta1 = theta
    
def get_points(theta):
    c1 = [math.sqrt(2) / 4 , - math.sqrt(2) / 4 * math.sin(theta) , math.sqrt(2) / 4 * math.cos(theta)]
    c2 = [0 , 1/2 * math.cos(theta) , 1/2 * math.sin(theta)]
    c3 = [math.sqrt(2) / 4 , math.sqrt(2) / 4 * math.sin(theta) , - math.sqrt(2) / 4 * math.cos(theta)]
    return c1, c2, c3

t = int(input())
for i in range(t):
    a = float(input())
    theta = get_angle(a)
    c1, c2, c3 = get_points(theta)
    
    print("Case #{}:".format(i+1))
    print(*c1)
    print(*c2)
    print(*c3)

