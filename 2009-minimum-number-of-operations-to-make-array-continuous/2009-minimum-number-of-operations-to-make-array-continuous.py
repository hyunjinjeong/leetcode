class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 모든 숫자가 unique여야 하고... 최댓값 - 최솟값이 len(nums) - 1이어야 함
        # 아니면 정렬을 하면?
        # 0번째가 최솟값 n-1번째가 최댓값
        # 아.. 숫자마다 right end가 정해져 있으니까 루프를 돌면서 찾으면 되는구나
        target = len(nums) - 1
        unique_nums = sorted(set(nums))

        # 2 3 5 11 15 이렇게 있고 7이라고 하면
        # 2에서 range_end는 9. count 1
        # 3에서 count 2, 5에서 count 3
        # 11에서 break임.
        # 그럼 2 3 4 5 6 7 8 9... 8개 중 3개가 있는 거니까 5개를 바꿔야 함. len(nums) - count.

        # res = max(unique_nums)
        # for i, left in enumerate(unique_nums):
        #     range_end = left + target
        #     count = 0

        #     for j in range(i, len(unique_nums)):
        #         right = unique_nums[j]
        #         if right > range_end:
        #             break
        #         count += 1
            
        #     res = min(len(nums) - count, res)
                
        # return res

        # 방향은 맞았는데 TLE가 뜬다. binary search를 쓰면 될 듯

        res = max(unique_nums)
        for i in range(len(unique_nums)):
            range_end = unique_nums[i] + target
        
            # binary search
            left, right = i, len(unique_nums)
            while left < right:
                mid = left + (right - left) // 2
                if unique_nums[mid] > range_end:
                    right = mid
                else:
                    left = mid + 1
            
            count = left - i
            res = min(len(nums) - count, res)
                
        return res