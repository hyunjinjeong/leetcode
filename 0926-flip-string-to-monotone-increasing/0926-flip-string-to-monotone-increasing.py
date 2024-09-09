class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # 뒤집었을 때 i번째에서 i-1까지의 substring은 monotone이라는 사실이 중요하네
        N = len(s)
        one_count = 0

        res = 0
        for c in s:
            if c == "1":
                one_count += 1
            # 0을 만나면 얘만 뒤집을지, 이전까지의 1을 다 뒤집을지...
            else:
                res = min(one_count, res + 1)

        return res