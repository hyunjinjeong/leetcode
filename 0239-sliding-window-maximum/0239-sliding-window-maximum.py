class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        
        # decreasing deque였나...
        for i in range(k-1):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

        ans = []
        for i in range(k-1, len(nums)):
            # 맨 왼쪽이 범위 벗어나면 pop. i - k + 1이 가장 왼쪽이니까...
            if dq and dq[0] == i - k:
                dq.popleft()

            # 현재 num보다 작은 element들은 모두 pop. decreasing 이기 때문에 오른쪽에서부터.
            while dq and nums[dq[-1]] < nums[i]: 
                dq.pop()
             
            dq.append(i)
            ans.append(nums[dq[0]])
        
        return ans