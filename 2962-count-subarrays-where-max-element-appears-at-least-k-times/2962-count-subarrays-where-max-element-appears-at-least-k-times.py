class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # max가 뭔지, 그리고 각각 index를 원패스로 구할 수 있음
        # 아.. 그냥 sliding window로 되는 구나
        # k개가 될 때까지 오른쪽으로 늘리다가
        # k개를 유지하면서 왼쪽을 줄이고
        # 다시 오른쪽을 늘리고
        max_num = max(nums)
        res = 0
        left = 0
        max_num_count = 0

        for right in range(len(nums)):
            if nums[right] == max_num:
                max_num_count += 1
            while max_num_count == k:
                if nums[left] == max_num:
                    max_num_count -= 1
                left += 1
            res += left
        
        return res