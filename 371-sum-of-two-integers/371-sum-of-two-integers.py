class Solution:
    def getSum(self, a: int, b: int) -> int:
        if not a:
            return b
        if not b:
            return a
        
        # mask 쓰는 이유는 https://leetcode.com/problems/sum-of-two-integers/discuss/776952/Python-BEST-LeetCode-371-Explanation-for-Python 참고..
        mask = 0xffffffff
        while b:
            _sum = (a^b) & mask
            carry = ((a&b) << 1) & mask
            
            a = _sum
            b = carry
        
        if (a>>31) & 1: # If a is negative in 32 bits sense
            return ~(a^mask)
        return a