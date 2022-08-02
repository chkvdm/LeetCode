# version1

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        srav = 1
        for n in prices:
            if prices.index(n) < (len(prices) - 1):
                if n >= prices[srav]:
                    srav +=1
                    prices[prices.index(n)] = 'x'
                else:
                    profit += (prices[srav] - n)
                    srav += 1
                    prices[prices.index(n)] = 'x'
        return profit


# version2

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(prices[n+1] - prices[n] for n in range(len(prices) - 1) if prices[n + 1] > prices[n])