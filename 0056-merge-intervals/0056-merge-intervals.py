class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = []
        ans.append(intervals[0])
        for i in range(1, len(intervals)):
            curr = intervals[i]
            last = ans[-1]

            if curr[0] <= last[1]:
                ans[-1][1] = max(last[1], curr[1])
            else:
                ans.append(curr)
        
        return ans