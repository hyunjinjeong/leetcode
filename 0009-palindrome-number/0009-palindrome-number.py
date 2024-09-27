class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_x = 0
        n = x
        while n:
            reversed_x = reversed_x * 10 + n % 10
            n //= 10
        
        return x == reversed_x