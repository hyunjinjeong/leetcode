class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 일단 MP 범위는 1 <= MP <= len(nums)+1임. 
        # tortoise hare 알고리즘으로 되려나..?
        # 근데 -가 있을 수 있고, num이 len(nums)보다 클 수 있음.
        # 일단 공간을 non-constant 쓰는 알고리즘을 생각해보자.
        # sort 후 찾는건 시간 O(nlogn)...
        # 1 ~ len(nums)까지를 key로 하는 dict 만들어서
        # 2-pass로 한번은 저장, 한번은 찾으면 공간 O(n?)
        dt = {}
        for num in nums:
            if 1 <= num <= len(nums)+1:
                dt[num] = True
        
        for num in range(1, len(nums)+2):
            if num not in dt:
                return num