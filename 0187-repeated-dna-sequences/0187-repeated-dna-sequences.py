class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = collections.defaultdict(int)

        res = []
        for i in range(len(s) - 9): # N이 딱 10이라고 하면 -10을 하면 안 되는구나
            seq = s[i:i + 10]
            seen[seq] += 1
            if seen[seq] == 2:
                res.append(seq)
        
        return res
