def fibonaccy(a):
    count = 0;
    number = 0
    number2 = 1
    if(a<=0):
        print('count number must be more than 0')
    elif(a==1):
        print(0)
    else:
        while count<a:
            print(number,end=" ")
            newNumber = number+number2;
            number = number2;
            number2 = newNumber;
            count = count+1;

def recursive(n):
    if n<=1:
        return n
    else:
        return recursive(n-1) + recursive(n-2)


if __name__ == "__main__":
    a = int(input('Enter count number: '))
    fibonaccy(a)
    print()
    for i in range(a):
        print(recursive(i),end=" ")
        