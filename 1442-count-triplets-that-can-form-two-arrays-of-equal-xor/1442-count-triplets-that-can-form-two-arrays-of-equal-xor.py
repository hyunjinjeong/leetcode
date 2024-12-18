class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        N = len(arr)
        res = 0

        for i in range(N - 1):
            xor = arr[i]
            for j in range(i + 1, N):
                xor ^= arr[j]
                if xor == 0:
                    res += j - i
        
        return res