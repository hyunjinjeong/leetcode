class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # 각각 갯수가 len(words)의 배수인지 보면 될 듯?
        counter = collections.defaultdict(int)

        for word in words:
            for c in word:
                counter[c] += 1

        for c in counter:
            if counter[c] < len(words) or counter[c] % len(words) != 0:
                return False
        
        return True