from math import gcd
from functools import reduce

def smallestMultiple(a,b):
    return a // gcd(a,b)*b



n = int(input("Smallest multiple for 1 through "))

print("is", reduce(smallestMultiple, range(n//2+1, n+1)))
