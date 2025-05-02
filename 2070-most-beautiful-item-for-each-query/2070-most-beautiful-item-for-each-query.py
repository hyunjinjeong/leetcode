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
            return lo
        
        items.sort(key=lambda tup: tup[0])

        max_beauties = [0]
        for price, beauty in items:
            max_beauties.append(max(beauty, max_beauties[-1]))

        res = []
        for target_price in queries:
            index = bisect_right(target_price)
            if index == -1:
                res.append(0)
            elif index == len(items):
                res.append(max_beauties[-1])
            else:
                res.append(max_beauties[index])
        return res
