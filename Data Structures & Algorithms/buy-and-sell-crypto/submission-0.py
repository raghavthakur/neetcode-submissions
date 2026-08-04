'''
price on ith day
buy first then sell later
return max profit or 0 from buying then selling

[10,1,5,6,7,1] -> 6
          i
buy on 1 and sell on 7

[10,8,7,5,2] -> 0
          i
do not buy

assume list is unordered
assume list can contain negative values

brute force: O(n^2)

sliding window
start=0
end
iterate through list to expand window end
check lowest value and update start
calc the diff between window end and window start and record max_profit seen so far

'''
# runtime: O(n) where n is length of prices
# space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        window_start = 0
        max_profit = 0

        for window_end in range(len(prices)):
            if prices[window_end] < prices[window_start]:
                window_start = window_end
            
            max_profit = max(max_profit, prices[window_end] - prices[window_start])
        
        return max_profit

'''
[10,1,5,6,7,1] -> 6
    s
            e

 mp=6

 [10,8,7,5,2] -> 0
           s
             e
mp=0
'''