class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # 일단 dict에 dict[a * b] = [(a, b)] 이런 식으로 저장해야 할 것 같은디
        # 그리고 돌면서 개수를 조합하면 되지 않을까
        dt = collections.defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                dt[nums[i] * nums[j]] += 1
        
        # 일단 (a, b), (c, d) 조합을 골라야 하니까 nC2 => n * (n - 1) // 2
        # 거기서 4개의 경우의 수가 나올 수 있음. abcd, abdc, bacd, badc. => 4
        # 그리고 (a, b)와 (c, d)가 스왑이 됨. => 2
        # => 4 * n * (n - 1)

        total = 0
        for tuple_count in dt.values():
            total += 4 * tuple_count * (tuple_count - 1)

        return total
