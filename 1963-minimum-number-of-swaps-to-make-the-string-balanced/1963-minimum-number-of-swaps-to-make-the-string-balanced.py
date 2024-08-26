class Solution:
    def minSwaps(self, s: str) -> int:
        # 이렇게 간단하다니;
        close, max_close = 0, 0

        for c in s:
            if c == "[":
                close -= 1
            else:
                close += 1
            
            max_close = max(close, max_close)
        
        return (max_close + 1) // 2