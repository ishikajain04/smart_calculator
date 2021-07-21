/* MATH OPERATIONS */


def add (a,b):
    return a+b
def sub (a,b):
    return a-b
def mul (a,b):
    return a*b
def div (a,b):
    return a/b
def mod(a,b):
    return a%b
def lcm (a,b):
    l=a if a>b else b
    while l<=a+b:
        if l%a==0 and l%b==0:
         return l
    l+=1
def hcf (a,b):
    h=a if a>b else b
    while h>=1:
        if h%a==0 and b%h==0:
         return h
    h-=1
