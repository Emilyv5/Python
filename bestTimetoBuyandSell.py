class Soution(object):
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        dp0 = [0]*len(prices)
        dp1 = [0]*len(prices)
        dp2 = [0]*len(prices)
        dp1[0] = -prices[0]
        dp2[0] = float('-inf')
        for i in range(1,len(prices)):
            dp0[i] = max(dp0[i-1], dp2[i-1])
            dp1[i] = max(dp1[i-1], dp0[i-1] - prices[i-1])
            dp2[i] = dp1[i] + prices[i]

        return max(dp0[len(prices)-1],dp2[len(prices)-1])
    
