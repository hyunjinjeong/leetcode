class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        counter = collections.Counter(words)
        return [common[0] for common in counter.most_common(k)]