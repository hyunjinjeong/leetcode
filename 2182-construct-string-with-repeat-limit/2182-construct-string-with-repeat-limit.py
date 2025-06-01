class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # heap?
        counter = collections.Counter(s)
        heap = [(-1 * ord(c), count) for c, count in counter.items()]
        heapq.heapify(heap)

        res = []
        while heap:
            ord_c, count = heapq.heappop(heap)
            c = chr(-1 * ord_c)
            
            use_count = min(count, repeatLimit)
            res.append(c * use_count)

            if count > use_count and heap:
                next_ord_c, next_count = heapq.heappop(heap)
                next_c = chr(-1 * next_ord_c)
                res.append(next_c)
                if next_count > 1:
                    heapq.heappush(heap, (next_ord_c, next_count - 1))

                heapq.heappush(heap, (ord_c, count - repeatLimit))                

        return "".join(res)
