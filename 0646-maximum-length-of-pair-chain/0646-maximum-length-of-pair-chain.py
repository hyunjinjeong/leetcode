class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # greedy도 되는구나
        pairs.sort(key=lambda p: p[1])

        curr = float("-inf")
        res = 0

        for left, right in pairs:
            if left > curr:
                res += 1
                curr = right
                
        return res