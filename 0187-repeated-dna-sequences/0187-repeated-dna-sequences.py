class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # two pointer 쓰면 될 듯? 길이 10을 유지하면서
        seen = collections.defaultdict(int)
        curr = collections.deque()

        for c in s:
            curr.append(c)
            if len(curr) == 10:
                word = ''.join(curr)
                seen[word] += 1
                curr.popleft()
        
        res = []
        for word in seen:
            if seen[word] >= 2:
                res.append(word)
        
        return res
