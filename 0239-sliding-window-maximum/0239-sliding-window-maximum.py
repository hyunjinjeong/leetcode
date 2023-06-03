class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Hint1: deque 써라. 어떻게?
        # decreasing deque 라고 한다.. 맨 왼쪽이 가장 큰 수
        deq = collections.deque()
        ans = []
        
        for i, num in enumerate(nums):
            # 현재 num보다 작은 element들은 모두 pop
            while deq and nums[deq[-1]] < num:
                deq.pop()
            
            deq.append(i) # 현재 index push
            if deq[0] == i - k: # 맨 왼쪽이 범위 벗어나면 pop
                deq.popleft()
            if i >= k - 1: # 이건 단순하게 k개 이후부터 정답에 넣기 위해...
                ans.append(nums[deq[0]])
        
        return ans