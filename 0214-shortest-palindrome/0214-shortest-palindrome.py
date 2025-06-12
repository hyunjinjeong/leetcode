class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # # 우선 확실한건 reverse(s)를 앞에 붙이면 무조건 palindrome임. 그러면 shortest는 그것보단 짧다
        # def is_palindrome(boundary):
        #     for i in range((boundary + 1) // 2):
        #         if s[i] != s[boundary - i]:
        #             return False
        #     return True
        
        # reversed_s = s[::-1]
        # for i in range(len(s) - 1, -1, -1):
        #     if is_palindrome(i):
        #         return reversed_s + s[i + 1:]

        # return ""

        reversed_s = s[::-1]

        for i in range(len(s) + 1):
            if s.startswith(reversed_s[i:]):
                return reversed_s[:i] + s
