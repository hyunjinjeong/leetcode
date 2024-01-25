class Solution:
    def validPalindrome(self, s: str) -> bool:
        # two pointer로 돌면서 palindrome이면 계속 진행하고
        # 아니면 left+1, right랑 left, right-1이랑 비교.
        # 최대 1번만 가능하니까... 이 값을 어디에 저장해야 하고
        # 매번 함수를 실행할 필요 없이 한 번만 하면 되는구나
        def is_palindrome(l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False

            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return is_palindrome(l+1, r) or is_palindrome(l, r-1)
        
        return True