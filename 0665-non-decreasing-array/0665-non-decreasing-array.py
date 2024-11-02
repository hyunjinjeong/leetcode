class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # 그냥 줄어드는 순간이 두 번 있으면 안 되는 거 아냐?
        # 아하 3 4 2 3 같은 경우도 안 되는구나
        # 하나를 고치는 건 결국 그 index만 없으면 sorted인지를 보는 거
        # 그러면 i에서 drop이 되는 경우, i - 1이 없으면 되는지 확인하면 되나?
        # 그럼 i - 2랑 i랑 비교하기?
        decreasing_count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                decreasing_count += 1
                left = nums[i - 1] if i > 0 else float("-inf")
                right = nums[i + 2] if i < len(nums) - 2 else float("inf")
                if left > nums[i + 1] and nums[i] > right:
                    return False
            
            if decreasing_count == 2:
                return False
        
        return True