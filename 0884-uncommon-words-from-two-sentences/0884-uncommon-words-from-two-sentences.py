class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counter = collections.defaultdict(int)
        
        for w in s1.split(" "):
            counter[w] += 1
        for w in s2.split(" "):
            counter[w] += 1
        
        return [w for w, count in counter.items() if count == 1]
