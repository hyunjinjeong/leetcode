class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # 이건 sliding window를 쓸 수 있나?
        # or은 줄지 않고 늘어나기만 하니까.. 작은 범위에서 만족하면 큰 범위에서도 만족함
        # 그럼 기존에 OR했던 결과는 어떻게 제외하지?
        # 3 2 1 4, k=5 라고 하면
        # 3에서 11, 2에서 11, 1에서 11, 4에서 111.
        # 이제 4에 도달하면 왼쪽을 줄여야 하는데, 11을 빼서 XOR하면 100이 되어버림.
        # 흠 각 비트별로 1의 개수를 저장하면 되긴 하는데 뭔가 비효율적인 것 같다. bitwise 연산으로 해결 가능한 방법이 없으려나
        # 일단 1의 개수 세서 ㄱㄱ
        one_counts = [0] * 30

        def update_one_count(num, delta):
            i = 0
            while num:
                if num & 1:
                    one_counts[i] += delta
                num >>= 1
                i += 1

        def get_or_sum():
            res = 0
            for i in range(len(one_counts)):
                if one_counts[i] > 0:
                    res |= 1 << i
            return res

        shortest = len(nums) + 1

        left = 0
        for right in range(len(nums)):
            update_one_count(nums[right], 1)
            while left <= right and get_or_sum() >= k:
                shortest = min(shortest, right - left + 1)
                update_one_count(nums[left], -1)
                left += 1

        return shortest if shortest <= len(nums) else -1
