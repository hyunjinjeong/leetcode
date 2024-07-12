class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # low가 odd면 +1하고 low+1으로
        # high가 odd면 +1하고 high-1으로
        # 그러면 두 짝수 사이의 홀수 갯수를 찾는 문제가 됨
        # high - odd에 // 2 하면 되는 듯?
        ans = 0

        if low % 2 == 1:
            ans += 1
            low += 1
        if high % 2 == 1:
            ans += 1
            high -= 1
        
        return ans + (high - low) // 2