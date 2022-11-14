class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False # 음수면 항상 False
        
        tmp = x
        reversed_num = 0
        
        # Reverse 해서 비교.
        while tmp > 0:
            reversed_num = reversed_num * 10 + tmp % 10 # 여기가 reverse하는 중요한 로직이구만.
            tmp = tmp // 10
            
        return x == reversed_num