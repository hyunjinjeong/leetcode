class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = [0] * (len(arr) + 1)
        for num in arr:
            if num > len(arr):
                continue
            freq[num] += 1
        
        for i in range(len(freq) - 1, 0, -1):
            if freq[i] == i:
                return i
        
        return -1
