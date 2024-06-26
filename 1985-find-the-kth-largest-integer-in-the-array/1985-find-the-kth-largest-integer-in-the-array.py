class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # 전부 int로 변환하고 찾을 수도 있을 거고..
        # 그러면 각 string 길이는 최대 100이니까 변환에 O(N)
        # sorting에 O(nlogn). 찾는건 O(1)
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        
        nums.sort()
        return str(nums[len(nums) - k])