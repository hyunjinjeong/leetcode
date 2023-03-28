class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str, k = "", 0
        
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                stack.append((curr_str, k))
                curr_str, k = "", 0
            elif c == "]":
                prev_str, prev_k = stack.pop()
                curr_str = prev_str + curr_str * prev_k
            else:
                curr_str += c
        
        return curr_str