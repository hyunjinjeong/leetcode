class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # square_nums = [num ** 2 for num in nums]
        # square_nums.sort()
        # return square_nums
        
        # O(n) 쏠루션을 찾아봅시다
        # 뭘 어떻게 하는거지 싶었는데 기존 배열이 정렬되어 있었다
        # 그럼 걍 절대값이 가장 낮은 숫자 인덱스를 찾고 거기서부터 투 포인터 돌리면 될 듯
        
        start = 0
        abs_num = float("inf")
        for i, num in enumerate(nums):
            if abs(num) < abs_num:
                abs_num = abs(num)
                start = i
        
        res = [nums[start] ** 2]

        left, right = start - 1, start + 1
        while left >= 0 or right < len(nums):
            if left < 0:
                res.append(nums[right] ** 2)
                right += 1
            elif right >= len(nums):
                res.append(nums[left] ** 2)
                left -= 1
            else:
                abs_left, abs_right = abs(nums[left]), abs(nums[right])
                if abs_left < abs_right:
                    res.append(nums[left] ** 2)
                    left -= 1
                else:
                    res.append(nums[right] ** 2)
                    right += 1
        
        return res
