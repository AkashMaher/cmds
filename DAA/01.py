profits, weights, capacity = [1, 6, 10, 16], [1, 2, 3, 5], 7


x = [-1]*(capacity+1)
dp = []
for i in range(len(profits)):
    dp.append(x)

def knap(index,remaincap):
    
    take = 0
    nottake = 0
    
    if remaincap <=0 or len(profits)<=index:
        return 0
    
    if dp[index][remaincap] != -1:
        return dp[index][remaincap]
    
    if remaincap>=weights[index]:
        take = profits[index] + knap(index+1,remaincap-weights[index])
    
    nottake = 0 + knap(index+1,remaincap)
    
    result = dp[index][remaincap] = max(take,nottake) 
    return result
print(knap(0,capacity))
