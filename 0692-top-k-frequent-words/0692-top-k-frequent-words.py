class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 대충 이걸 직접 짜서 해야 됨
        counter = collections.Counter(words)
        sorted_counter = sorted(counter.items(), key=lambda tup: (-tup[1], tup[0]))
        return [tup[0] for tup in sorted_counter[:k]]
    
        
    
    