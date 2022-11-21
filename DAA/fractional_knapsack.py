def fractional():
    weight = [10,20,30]
    value = [60,100,120]
    WT = 50
    res = 0.0
    
    for pair in sorted(zip(weight, value), key=lambda x:x[1]/x[0], reverse=True):
        if(WT<=0):
            break
        if WT<pair[0]:
            res += (WT * pair[1]/pair[0])
            WT = 0
        else :
            WT -= pair[0]
            res += pair[1]
    print(res)
        
fractional() 



   