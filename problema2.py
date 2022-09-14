a=int(input("a="))
b=int(input("b="))
fact=1

def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact*=i
    return fact
if (a>b):
    print("c=",factorial(a)/(factorial(b)*(factorial(a-b))))
else:
    print("functia nu e definita")