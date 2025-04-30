class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # 구간 내의 max - min <= limit 이어야 함
        # sliding window? max랑 min을 저장하고
        # 식을 만족할 때까지 오른쪽을 늘리고, 만족 안하면 다시 만족할 때까지 왼쪽을 늘리고.
        # 결과적으로 양 끝이 max 혹은 min으로 유지되면서 윈도우가 이동할 것 같음
        # 그러면 2번째 max나 min은 어떻게 구하지..? heap 같은걸 들고 있어야 하나
        
        # max_heap, min_heap = [], []
        # longest = 0

        # left = 0
        # for right in range(len(nums)):
        #     heapq.heappush(max_heap, (-nums[right], right))
        #     heapq.heappush(min_heap, (nums[right], right))
            
        #     while -max_heap[0][0] - min_heap[0][0] > limit:
        #         left = min(max_heap[0][1], min_heap[0][1]) + 1
        #         while max_heap[0][1] < left:
        #             heapq.heappop(max_heap)
        #         while min_heap[0][1] < left:
        #             heapq.heappop(min_heap)

        #     longest = max(longest, right - left + 1)

        # return longest

        # monotonic deque를 사용하는 방법이 있다.
        max_deque, min_deque = collections.deque(), collections.deque()
        longest = 0

        left = 0
        for right in range(len(nums)):
            while max_deque and max_deque[-1] < nums[right]:
                max_deque.pop()
            max_deque.append(nums[right])

            while min_deque and min_deque[-1] > nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])

            while max_deque[0] - min_deque[0] > limit:
                if nums[left] == max_deque[0]:
                    max_deque.popleft()
                if nums[left] == min_deque[0]:
                    min_deque.popleft()
                left += 1
            
            longest = max(longest, right - left + 1)
        
        return longest
