class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # brute force는 쉬운데.. 아마 최적화를 해야 하는 듯
        # binary search를 쓰는 거 같다. potion의 순서는 상관 없으니까 정렬해두고,
        # spells를 돌면서 success를 넘는 index를 찾으면 될 듯
        res = []
        potions.sort()

        for spell in spells:
            left, right = 0, len(potions)
            while left < right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    right = mid
                else:
                    left = mid + 1

            res.append(len(potions) - left)
        
        return res