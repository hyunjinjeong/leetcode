class Solution:
    def minOperations(self, s: str) -> int:
        start_one_count, start_zero_count = 0, 0
        for i, c in enumerate(s):
            if i % 2 == 0:
                if c == "1":
                    start_zero_count += 1
                else:
                    start_one_count += 1
            else:
                if c == "1":
                    start_one_count += 1
                else:
                    start_zero_count += 1
        
        return min(start_one_count, start_zero_count)