class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        N = len(arr)
        res = 0

        for i in range(N - 1):
            xor = arr[i]
            for k in range(i + 1, N):
                xor ^= arr[k]
                if xor == 0:
                    res += k - i
        
        return res