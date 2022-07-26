class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lows,highs = [],[]
        low,high = 100000,0

        for i in range(len(prices)):
            j = len(prices)-1-i
            if prices[i]<low:
                low = prices[i]
            if prices[j]>high:
                high = prices[j]
            lows.append(low)
            highs.append(high)
        
        diff = []
        for i in range(len(prices)):
            j = len(prices)-1-i
            diff.append(highs[j]-lows[i])

        print(max(diff))

        return max(diff)
        
sol = Solution()
sol.maxProfit([7,1,5,3,6,4])
sol.maxProfit(prices = [7,6,4,3,1])