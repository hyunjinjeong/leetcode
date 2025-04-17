class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # 특정 num에 대해서 [num - limit, num + limit] 범위로 swap 가능
        # 당연히 작은 숫자일수록 왼쪽에 와야 하는데
        # swap이라고 생각하니 어려운 것 같은데... 모르겠다 이건
        # grouping 하면 되는구나
        groups = []
        num_to_group_index = {}

        prev = float("-inf")
        group_index = -1
        for curr in sorted(nums):
            if curr - prev > limit:
                groups.append(collections.deque())
                group_index += 1
            
            groups[group_index].append(curr)
            num_to_group_index[curr] = group_index
            prev = curr

        for i, num in enumerate(nums):
            group = groups[num_to_group_index[num]]
            nums[i] = group.popleft()
        
        return nums
