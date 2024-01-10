class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # brute force로 하면 걍 모든 조합 돌면서 구하는거고..
        # 모르겠다.. 아니 이게 medium?
        merged = sorted(zip(nums1, nums2), key=lambda pair: pair[1], reverse=True)

        # nums2를 돌면 nums2[i]가 min으로 고정됨
        # 그러면 nums1에서의 최대를 구해야 하는데, 이걸 min heap으로..!
        ans = 0
        nums1_sum = 0
        heap = []

        for num1, num2 in merged:
            nums1_sum += num1
            heapq.heappush(heap, num1)

            if len(heap) > k:
                nums1_sum -= heapq.heappop(heap)
            if len(heap) == k:
                ans = max(nums1_sum * num2, ans)
            
        return ans
        