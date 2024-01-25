class Solution:
    def validPalindrome(self, s: str) -> bool:
        # two pointer로 돌면서 palindrome이면 계속 진행하고
        # 아니면 left+1, right랑 left, right-1이랑 비교.
        # 최대 1번만 가능하니까... 이 값을 어디에 저장해야 하고
        def is_palindrome(l, r, has_deleted):
            if l >= r:
                return True
            
            c1, c2 = s[l], s[r]
            if c1 == c2:
                return is_palindrome(l+1, r-1, has_deleted)
            
            if has_deleted:
                return False

            return is_palindrome(l+1, r, True) or is_palindrome(l, r-1, True)
        
        return is_palindrome(0, len(s)-1, False)