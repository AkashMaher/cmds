profits, weights, capacity = [1, 6, 10, 16], [1, 2, 3, 5], 7
length = len(profits)

#print(knap(0,capacity))
x = [-1] * (capacity + 1)
dp = []
for _ in range(len(profits)):
    dp.append(x)
    
    
def knap(index, cap):
    take = 0
    notTake = 0
    # base condition
    if cap <= 0 or index >= length:
        return 0

    #check if we have calculated before
    if dp[index][cap] != -1:
        return dp[index][cap]

    #check for overflow before taking and adding
    if weights[index] <= cap:
        take = profits[index] + knap(index+1, cap-weights[index])
    notTake = knap(index+1, cap)

    result = dp[index][cap] = max(take,notTake)
    print(dp[index][cap])
    return result

print(knap(0,capacity))
