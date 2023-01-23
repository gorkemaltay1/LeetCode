class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        paying = []
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    paying.append(prices[i]-prices[j])
                    break
                elif prices[i]<prices[j] and j == len(prices)-1:
                    paying.append(prices[i])
        return paying + [prices[-1]]