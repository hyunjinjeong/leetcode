class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # 같은 숫자로 xor를 두번 하면? x^k^k. k^k == 0이니까 x^0 == x.
        # 특정 숫자가 가질 수 있는 값은 기존 값이랑 k와 xor했을 때의 값밖에 없음
        # 모든 숫자에 대해서 max(num, num^k)을 sum으로 사용하면 되지 않을까?
        # 흠.. 틀린 답이 있는거 보면 특정 숫자가 하나의 값만 가지는 경우의 수가 있나 봄
        # 아 홀수 짝수에 따라 다른걸 간과함...
        res = 0

        xor_count = 0
        smallest_diff = float("inf")
        for num in nums:
            xor_num = num ^ k
            if xor_num > num:
                res += xor_num
                xor_count += 1
                smallest_diff = min(xor_num - num, smallest_diff)
            else:
                res += num
                smallest_diff = min(num - xor_num, smallest_diff)
        
        return res if xor_count % 2 == 0 else res - smallest_diff