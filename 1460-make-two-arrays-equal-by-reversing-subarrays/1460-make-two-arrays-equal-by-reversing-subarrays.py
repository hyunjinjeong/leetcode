class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count = [0] * 1001

        for num in target:
            count[num] += 1
        for num in arr:
            count[num] -= 1
        
        for num in count:
            if num != 0:
                return False
        return True