class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # 길이 3 이상, 모든 연속된 숫자들의 차이가 같아야 함. 같은 조합이 여러번 나와도 상관 없고...
        # 베이스가 길이 2짜리여야 하나? nC2니까 O(n^2)이긴 한데 1000개라서 괜춘
        # 1개씩 고려한다고 하면 어떻게 하지?
        # 일단 시작은 0에서 n-3까지만 돌아야 함. 길이가 최소 3이니까

        N = len(nums)

        @cache
        def dfs(last, diff):
            res = 0
            for i in range(last + 1, N):
                if nums[i] - nums[last] == diff:
                    res += 1 + dfs(i, diff)
            return res
                
        res = 0
        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                # 여기서 top down dp를 적용할 수 있으려나?
                # i, j 값을 함수에 넣어줘야 하나? ㄴㄴ
                # diff랑 start 값만 넣고 pick & not pick 넣으면 되지 않을까?
                # 아 근데 뺄 대상이 필요함. j는 넣어야겠다.
                res += dfs(j, nums[j] - nums[i])
        return res