class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 일단 MP 범위는 1 <= MP <= len(nums)+1임. 
        # 일단 공간을 non-constant 쓰는 알고리즘을 생각해보자.
        # 1 ~ len(nums)까지를 key로 하는 dict 만들어서
        # 2-pass로 한번은 저장, 한번은 찾으면 공간 O(n?)
        # 저장하는걸 nums 에다가 하면 되겠는데
        
        # 각 숫자를 해당 index로 move. e.g. 1->0, 5->4 ...
        # 여기서 잘 안됐는데 nums[i]를 num으로 변수 저장해둔게 문제였음..
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        
        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        
        # for문에서 안 걸리면 1~len(nums)까지 꽉 차있는거
        return len(nums) + 1