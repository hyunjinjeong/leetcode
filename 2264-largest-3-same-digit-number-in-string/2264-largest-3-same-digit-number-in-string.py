class Solution:
    def largestGoodInteger(self, num: str) -> str:
        left, right = 0, 0
        ans = -1

        for i in range(len(num) - 2):
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                ans = max(int(num[i]), ans)
        
        return str(ans) * 3 if ans != -1 else ""