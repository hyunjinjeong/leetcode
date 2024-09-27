class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = collections.Counter(s)

        for c in t:
            counter[c] -= 1
            if counter[c] < 0:
                return c