class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # 일단 최댓값은 max(nums)인 것 같고...
        # sorting, stack 이런 류는 못 쓰는 문제일 것 같음
        # two pointer?도 아닌 것 같고
        # dp 아니면 greedy?
        # dp는 아닌 것 같은데 문제를 작은 부분으로 나눌 방법이 없음
        # 그러면 greedy?
        # prefix sum, binary search를 간과했구나.
        total_sum = 0
        ans = 0

        for i, num in enumerate(nums):
            total_sum += num
            ans = max((total_sum + i) // (i + 1), ans)
        
        return ans