class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # range를 가지고 있고..
        # 문제는 이 range에 k개의 리스트의 아이템이 하나씩 들어간다는 걸 확인해야 함.
        # heap을 어떻게 쓰면 될 것 같은데
        # heap에서 원소를 빼면서 range를 업데이트. smallest는 ans로 들고 있으면 됨.
        
        # 일단 처음에 0번째 원소들을 다 heap에 넣은 뒤에 빼면 초기 range는 완성이 됨
        # 그 다음이 문제인데
        # heap에 넣을 때 몇번째 리스트인지를 tuple로 같이 넣어주면
        # 하나 빼고, 그 다음에는 해당 리스트에서 또 heap을 넣어주고 이러면 되지 않으려나?
        
        
        heap = []
        right = float("-inf")
        for i, lst in enumerate(nums):
            num = lst[0]
            heapq.heappush(heap, (num, i, 0))
            right = max(right, num)
        
        ans = [float("-inf"), float("inf")]
        while heap:
            left, i, j = heapq.heappop(heap)
            if right - left < ans[1] - ans[0]: # 길이가 같으면 기존꺼 유지
                ans = [left, right]
            
            if j + 1 == len(nums[i]):
                break
            
            # pop된 리스트에서 넣기
            num = nums[i][j+1]
            right = max(right, num)
            heapq.heappush(heap, (num, i, j+1))
        
        return ans