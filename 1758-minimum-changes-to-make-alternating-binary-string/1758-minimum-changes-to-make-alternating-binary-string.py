class Solution:
    def minOperations(self, s: str) -> int:
        # 이게 easy..?
        # greedy로 되는 건가
        start_one = "1"
        start_zero = "0"

        start_one_count, start_zero_count = 0, 0
        for c in s:
            if c != start_one:
                start_one_count += 1
            if c != start_zero:
                start_zero_count += 1
            
            start_one = "0" if start_one == "1" else "1"
            start_zero = "0" if start_zero == "1" else "1"
        
        return min(start_one_count, start_zero_count)