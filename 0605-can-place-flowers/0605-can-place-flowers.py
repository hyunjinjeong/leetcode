class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 흠..? 그냥 greedy로 돌면 되나
        # i번째일때 i-1과 i+1이 0이면 됨.
        # 예외: 0일때랑 n-1일 때.
        if n == 0:
            return True
        
        if len(flowerbed) == 1:
            return flowerbed[0] == 0
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
                
            if len(flowerbed) >= 2 and i == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            elif len(flowerbed) >= 2 and i == len(flowerbed) - 1 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                n -= 1
            elif len(flowerbed) >= 3 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            
            if n == 0:
                break
        
        return n == 0