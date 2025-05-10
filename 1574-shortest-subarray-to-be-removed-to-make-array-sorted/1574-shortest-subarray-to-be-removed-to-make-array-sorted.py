class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # non-decreasing subarray..를 시작과 끝에서 찾고
        # 두 subarray가 정렬되도록 만들기?
        left_end = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                break
            left_end = i
        
        right_start = len(arr) - 1
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                break
            right_start = i
        
        if left_end == len(arr) - 1: # already
            return 0

        # 여기서 최종 subarray는 어떻게 정하지
        # 1 2 3 10
        # 2 3 5
        # 양쪽을 하나씩 쌓아가면 되는구나
        res = right_start

        left, right = 0, right_start
        while left <= left_end:
            while right < len(arr) and arr[left] > arr[right]:
                right += 1
            res = min(res, right - left - 1)
            left += 1
        
        return res
