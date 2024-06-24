class Solution:
    def frequencySort(self, s: str) -> str:
        # heap을 쓸 수도 있구낭
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        heap = [(-v, k) for k, v in freq.items()]
        heapq.heapify(heap)

        ans = []
        while heap:
            count, c = heapq.heappop(heap)
            ans.append(c * -count)

        return "".join(ans)