class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 그냥 counter 만들어서 하면 되는데.. 그건 easy고
        # O(N) time, O(1) space에 하는게 medium인가
        # 요거 정답이 최대 2개임. 1/3 보다 많이 등장해야 하니까.
        # 그 무슨 알고리즘이 있었던거 같은데... 최대 갯수를 variable로 저장해서 뺴고 더하고 했던..
        # Boyer-Moore Voting Algorithm이라고 하는구나. 그런데 그건 과반수에 대해서 동작하는 알고리즘인데
        # 1/3에 대해서는 어떻게..?

        total_count = len(nums)
        first, second = None, None
        first_count, second_count = 0, 0

        for num in nums:
            if num == first:
                first_count += 1
            elif num == second:
                second_count += 1
            elif first_count == 0:
                first = num
                first_count = 1
            elif second_count == 0:
                second = num
                second_count = 1
            else:
                first_count -= 1
                second_count -= 1

        first_count, second_count = 0, 0
        for num in nums:
            if num == first:
                first_count += 1
            elif num == second:
                second_count += 1

        res = []
        if first_count > total_count // 3:
            res.append(first)
        if second_count > total_count // 3:
            res.append(second)

        return res
