def maxProfit(prices):
    i = 1
    j = 2
    m = {}

    for i in range(1,len(prices)):
        for j in range(2,len(prices)):
            if prices[j] > prices[i]:
                print(i, j)
                m = prices[j] - prices[i]
                j +=1
                print(m)
                print(prices[i], prices[j], m)
        j+=1
        i+=1
    

prices = [7,1,5,3,6,4]
maxProfit(prices)