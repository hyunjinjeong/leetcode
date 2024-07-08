class Solution:
    def totalMoney(self, n: int) -> int:
        # 이건 수학문젠가... 뭐지
        # 일단 정석적으로 ㄱㄱ
        ans = 0
        prev_monday = 0
        curr = 0

        for day in range(n):
            if day % 7 == 0:
                curr = prev_monday + 1
                prev_monday += 1
            else:
                curr += 1
            ans += curr
        
        return ans