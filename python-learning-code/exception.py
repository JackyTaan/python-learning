from math import pi as p
import math as ma
import os 
import sys


def exc_test(n,m):
    try:
        print('aa')
        return 5/1
    except Exception as e:
        print(e)


d = exc_test(3,2)
print(d)

print(ma.__name__)

print(os.getcwd())
print('-------------')
print(sys.path)
print('-------------')
