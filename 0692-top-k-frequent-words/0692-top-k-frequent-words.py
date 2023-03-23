class Item:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    
    def __lt__(self, other):
        if self.freq == other.freq:
            # 최소 힙에서 하나씩 꺼내서 reverse 하니까.. 크기를 반대로 해놓음.
            return self.word > other.word
        return self.freq < other.freq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = {}
        for word in words:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
        
        # heap에서 두 가지 기준으로 비교해야 하는데... 스스로 클래스를 만들면 됨!
        heap = []
        for word, freq in counter.items():
            item = Item(word, freq)
            heapq.heappush(heap, item)
            if len(heap) > k: # O(nlogk) 위해서 크기를 k로 고정
                heapq.heappop(heap)
        
        # 최소 힙이니까 하나씩 꺼내서 거꾸로.
        ans = []
        while heap:
            ans.append(heapq.heappop(heap).word)
        return ans[::-1]