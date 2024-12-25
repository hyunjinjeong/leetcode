class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # two pointer 쓰면 될 듯? 길이 10을 유지하면서
        seen = collections.defaultdict(int)
        curr = ''

        for right, c in enumerate(s):
            curr += c
            if len(curr) == 10:
                seen[word] += 1
                curr = curr[1:]
        
        res = []
        for word in seen:
            if seen[word] >= 2:
                res.append(word)
        
        return res
