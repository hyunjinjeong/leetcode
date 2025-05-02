class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # X보다 작은 price를 찾아야 함. 그 중 beauty가 가장 커야 함.
        # 정렬하고 나서 binary search 돌리면 될 듯?
        def bisect_right(target_price):
            lo, hi = 0, len(items)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if target_price >= items[mid][0]:
                    lo = mid + 1
                else:
                    hi = mid
            
            index = lo - 1
            return items[index][1] if index >= 0 else 0
        
        items.sort(key=lambda tup: tup[0])
        max_beauty = items[0][1]
        for i in range(1, len(items)):
            items[i][1] = max(items[i][1], items[i - 1][1])

        return [bisect_right(target_price) for target_price in queries]
