class Solution:
    def myAtoi(self, s: str) -> int:
        value, state, pos, sign = 0, 0, 0, 1
        INT_MAX, INT_MIN = 2**31-1, -2**31

        if len(s) == 0:
            return 0

        # DFA 버전
        for i, c in enumerate(s):
            if state == 0:
                if c == " ":
                    continue
                elif c in ("+", "-"):
                    sign = 1 if c == "+" else -1
                    state = 1
                elif c.isdigit():
                    digit = ord(c) - ord('0') # int 구하는 트릭. 
                    value = value * 10 + digit
                    state = 2
                else:
                    return 0
            elif state == 1:
                if c.isdigit():
                    digit = ord(c) - ord('0')
                    value = value * 10 + digit
                    state = 2
                else:
                    return 0
            elif state == 2:
                if c.isdigit():
                    digit = ord(c) - ord('0')
                    # overflow 체크
                    if value > INT_MAX // 10 or (value == INT_MAX // 10 and digit > INT_MAX % 10):
                        return INT_MAX if sign == 1 else INT_MIN
                    value = value * 10 + digit
                else:
                    break

        return sign * value