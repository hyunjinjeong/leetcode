class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # ㅇㅎ 인접한 인덱스만 보는게 아니라 전체가 대상임
        # sorting은 아니고
        # two pointer? dp? greedy?
        # greedy는 안되넹
        # monotonic stack?
        stack = []

        max_right = float("-inf")

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if num < max_right:
                return True
            
            while stack and stack[-1] < num:
                max_right = stack.pop()
            
            stack.append(num)

        return False