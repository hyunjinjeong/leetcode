class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        
        # decreasing deque였나...
        for i in range(k-1):
            while dq and nums[dq[-1]] < nums[i]: # 현재 num보다 작은 element들은 모두 pop
                dq.pop()
            dq.append(i)

        ans = []
        for i in range(k-1, len(nums)):
            if dq and dq[0] == i - k: # 맨 왼쪽이 범위 벗어나면 pop
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i]: # 현재 num보다 작은 element들은 모두 pop
                dq.pop()
             
            dq.append(i)
            ans.append(nums[dq[0]])
        
        return ans