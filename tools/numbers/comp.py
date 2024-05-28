# tools/numbers/comp.py

def sumofdigits(n):
    return sum(int(digit) for digit in str(n))

def ispal(n):
    s = str(n)
    return s == s[::-1]
