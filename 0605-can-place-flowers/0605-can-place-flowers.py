class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new_flower_bed = [0] + flowerbed + [0]
        
        for i in range(1, len(flowerbed) + 1):
            if new_flower_bed[i-1] == 0 and new_flower_bed[i] == 0 and new_flower_bed[i+1] == 0:
                new_flower_bed[i] = 1
                n -= 1
            
            if n <= 0:
                return True
        
        return False