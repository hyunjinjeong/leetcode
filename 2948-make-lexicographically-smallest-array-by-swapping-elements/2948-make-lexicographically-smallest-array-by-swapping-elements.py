class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # 특정 num에 대해서 [num - limit, num + limit] 범위로 swap 가능
        # 당연히 작은 숫자일수록 왼쪽에 와야 하는데
        # swap이라고 생각하니 어려운 것 같은데... 모르겠다 이건
        # grouping 하면 되는구나
        groups = []
        num_to_group_index = {}
        index_to_num = {i: num for i, num in enumerate(nums)}

        nums.sort()

        prev = float("-inf")
        group_index = -1
        for i, curr in enumerate(nums):
            if curr - prev > limit:
                groups.append(collections.deque())
                group_index += 1
            
            groups[group_index].append(curr)
            num_to_group_index[curr] = group_index
            prev = curr

        for i in range(len(nums)):
            num = index_to_num[i]
            group = groups[num_to_group_index[num]]
            sorted_num = group.popleft()
            nums[i] = sorted_num
        
        return nums
