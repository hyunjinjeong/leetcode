class Solution:
    def minDeletions(self, s: str) -> int:
        # 정렬도 필요 없네
        res = 0
        freq = collections.Counter(s)

        freq_set = set()
        for val in freq.values():
            while val and val in freq_set:
                val -= 1
                res += 1
            freq_set.add(val)
        
        return res