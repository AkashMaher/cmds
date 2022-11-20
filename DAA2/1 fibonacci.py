def fibo1(n):
    
    if n == 0:
        print(0)
        return
    if n == 0:
        print(1)
        return
    
    i = 0
    n1 = 0
    n2 = 1
    print(n1, n2, end=" ")
    n = n - 2
    while i < n:
        new = n1 + n2
        print(new, end=" ")
        n1 = n2
        n2 = new
        i += 1  


def fibo2(n1,n2,len):
    if len == 0:
        return 
    new = n1+n2
    print(new, end=" ")
    fibo2(n2,new,len-1)

fibo1(7)
print()
print(0, 1, end=" ")
len = 7
fibo2(0, 1, 7 - 2)
