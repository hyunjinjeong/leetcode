class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 갯수가 k개가 되면 종료하는 backtracking을 돌려야 하는데
        self.res = []

        def backtrack(start, current):
            if len(current) == k:
                self.res.append(current[:])
                return

            for i in range(start, n + 1):
                current.append(i)
                backtrack(i + 1, current)
                current.pop()

        backtrack(1, [])
        return self.res