class Solution:
    def myAtoi(self, s: str) -> int:
        l, r = 0, 0

        # 1. Ignore leading whitespaces
        while l < len(s) and s[l] == " ":
            l += 1
            r = l

        # 2. Check the sign character
        if l < len(s) and s[l] in ("+", "-"):
            r += 1

        # 3. Read the digit characters        
        while r < len(s) and s[r].isdigit():
            r += 1

        # 4. Convert the digits into an integer
        res_str = s[l:r]
        try:
            res = int(res_str)
        except:
            res = 0

        # 5. Clamp the integer
        if res >= 2**31-1:
            res = 2**31 - 1
        elif res < -2**31:
            res = -2**31

        return res