class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # 느낌이 i가 높을수록 gcd가 높은 조합을 써야 하는거 같은데
        # 최대 길이가 14니까 모든 쌍에 대해서 GCD를 구할 수는 있음
        # 근데 그 다음에는 어떻게 하지? 그냥 모든 경우의 수를 다 해봐야 하나?
        # 정렬이 도움이 될까? 정렬해서 (i, j)에서 i < j 인 경우 gcd의 최댓값이 nums[i]. 딱히 도움은 안 되는 것 같다.
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # cache 쓰려면 tuple로 변환해야 함.. bitmask는 포기 ㅈㅈ
        @cache
        def backtrack(i, nums):
            if not nums:
                return 0

            max_score = 0
            for x in range(len(nums)):
                for y in range(x + 1, len(nums)):
                    new_nums = nums[:x] + nums[x+1:y] + nums[y+1:]
                    curr_score = i * gcd(nums[x], nums[y]) + backtrack(i + 1, new_nums)
                    max_score = max(max_score, curr_score)
            
            return max_score

        return backtrack(1, tuple(nums))
