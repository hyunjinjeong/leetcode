class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 아 monotonic stack 이용하면 됨
        next_gt = {}
        stack = []

        for i, num2 in enumerate(nums2):
            while stack and num2 > stack[-1]:
                next_gt[stack[-1]] = num2
                stack.pop()
            stack.append(num2)
        
        for num2 in stack: # next_gt가 없는 경우
            next_gt[num2] = -1

        ans = []
        for num1 in nums1:
            ans.append(next_gt[num1])
        
        return ans