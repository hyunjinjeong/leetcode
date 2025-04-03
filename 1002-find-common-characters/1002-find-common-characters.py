class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = collections.defaultdict(int)
        for c in words[0]:
            counter[c] += 1

        for i in range(1, len(words)):
            new_counter = collections.defaultdict(int)
            for c in words[i]:
                new_counter[c] += 1
            
            for c in counter:
                counter[c] = min(counter[c], new_counter[c])

        res = []
        for c in counter:
            for _ in range(counter[c]):
                res.append(c)
        return res