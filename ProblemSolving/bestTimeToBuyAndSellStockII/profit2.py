class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        mini = float('inf')
        profit = 0
        for i in range(len(prices)):
            if prices[i] <= mini:
                mini = prices[i]
            else:
                if (i+1 < len(prices) and prices[i+1] < prices[i]) or i == len(prices)-1:
                    profit += prices[i]-mini
                    mini = float('inf')
        return profit
        
        """
        # Go Greedy
        
        # Assume minimum is day1 
        
        mini = float('inf')
        total = 0
        
        # Iterate through the day prices
        for day in range(len(prices)):
            
            # Change the minimum and buy that day
            if prices[day] < mini:
                mini = prices[day]
            elif (day+1 < len(prices) and prices[day+1] < prices[day]) or day == len(prices)-1:
                #print(prices[day]-mini)
                total += prices[day]-mini
                mini = float('inf')
            #print(mini, prices[day])
        return total
        """
