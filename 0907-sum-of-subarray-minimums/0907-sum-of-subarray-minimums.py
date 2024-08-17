class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # ..? monotonic stack으로 풀 수 있었음
        MOD = 10**9 + 7
        N = len(arr)

        stack = []
        res = [0] * N

        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                stack.pop()
            
            if stack:
                prev_index = stack[-1]
                res[i] = (res[prev_index] + num * (i - prev_index)) % MOD
            else:
                res[i] = (num * (i + 1)) % MOD
            
            stack.append(i)
        
        return sum(res) % MOD