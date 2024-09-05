class Solution:
    def minimumLength(self, s: str) -> int:
        # 뭐지 이건... 그냥 구현 문제 아닌가?
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            c = s[left]

            while left <= right and s[left] == c:
                left += 1
            while left < right and s[right] == c:
                right -= 1
    
        return right - left + 1