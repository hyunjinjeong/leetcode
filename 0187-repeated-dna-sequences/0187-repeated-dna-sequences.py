class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = collections.defaultdict(int)

        res = []
        for i in range(len(s) - 10):
            seq = s[i:i + 10]
            seen[seq] += 1
            if seen[seq] == 2:
                res.append(seq)
        
        return res
