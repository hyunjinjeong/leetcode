class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # subarray니까 정렬은 못 쓰고
        # 그냥 슬라이딩 윈도우로 순회하면서 봐야할 듯?
        # 계산을 재활용할 방법이... 그냥 빠지는거 빼고 들어오는거 더해서 값이 k * threshold 보다 큰지 보면 될 듯?

        # 일단 첫번째는 스페셜 케이스로 미리 계산하자
        # array를 만들 필요도 없구나..? sum만 계산하면 됨.
        TARGET = k * threshold
        ans = 0

        sub_sum = 0
        for i in range(k):
            sub_sum += arr[i]
        
        if sub_sum >= TARGET:
            ans += 1
        
        for i in range(k, len(arr)):
            sub_sum = sub_sum - arr[i - k] + arr[i]
            if sub_sum >= TARGET:
                ans += 1
        
        return ans
