class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []

        for i in range(len(prices)):
            price = prices[i]
            
            for j in range(i + 1, len(prices)):
                if prices[j] <= price:
                    price -= prices[j]
                    break
            
            res.append(price)
        
        return res
