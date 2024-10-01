class Solution:
    def reorganizeString(self, s: str) -> str:
        # heap 쓰면 되려나?
        # 하나 뽑고.. 그게 마지막 캐릭터랑 같으면 하나 더 뽑고. 그 다음 처음 뽑았던거 다시 넣고.
        # 만약 하나 더 뽑을게 없으면 불가능한거니까 "" 리턴하고.

        counter = [0] * 26
        for c in s:
            i = ord(c) - ord("a")
            counter[i] += 1
        
        heap = []
        for i in range(26):
            if counter[i] == 0:
                continue
            c = chr(i + ord("a"))
            heapq.heappush(heap, (-counter[i], c))
        
        res = []
        while heap:
            first, char1 = heapq.heappop(heap)
            if res and char1 == res[-1]:
                if not heap:
                    return ""
                second, char2 = heapq.heappop(heap)
                res.append(char2)
                if second < -1:
                    heapq.heappush(heap, (second + 1, char2))
            
            res.append(char1)
            if first < -1:
                heapq.heappush(heap, (first + 1, char1))
        
        return "".join(res)