class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        curr = newInterval

        for interval in intervals:
            if interval[1] < curr[0]:
                left.append(interval)
            elif interval[0] > curr[1]:
                right.append(interval)
            else:
                curr = [min(interval[0], curr[0]), max(interval[1], curr[1])]
        
        return left + [curr] + right