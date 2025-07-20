class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # 음수도 있어서 sliding window는 불가능
        # brute force는? 이중 루프니까 O(N^2). 이것보다 좋은 방법을 써야 함
        # binary search? prefix sum?
        # dp랑 binary는 안 되겠다
        # monotonic stack을 사용하는 거였음. 이걸 어케 푸냐..
        N = len(nums)

        prefix_sum = [0] * (N + 1)
        for i in range(N):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        min_length = N + 1

        # preifx_sum[j] - prefix_sum[i] >= k 를 찾아야 
        monotonic_deque = collections.deque()
        for j in range(N + 1):
            while monotonic_deque and prefix_sum[j] - prefix_sum[monotonic_deque[0]] >= k:
                i = monotonic_deque.popleft()
                min_length = min(min_length, j - i)

            while monotonic_deque and prefix_sum[j] <= prefix_sum[monotonic_deque[-1]]:
                monotonic_deque.pop()
            
            monotonic_deque.append(j)
        
        return min_length if min_length <= N else -1
