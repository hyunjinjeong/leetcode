class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # ??
        # 일단 토큰을 정렬해야하는 것 같음
        tokens.sort()

        # 보니까 항상 play를 해야하는 건 아닌 것 같다.
        lo, hi = 0, len(tokens) - 1
        res, cur = 0, 0

        # power >= tokens[lo]면 왼쪽 face up 하고
        # 아니면 face down 하고?
        while lo <= hi:
            if power >= tokens[lo]:
                power -= tokens[lo]
                lo += 1
                cur += 1
            else:
                power += tokens[hi]
                hi -= 1
                cur -= 1
            
            res = max(res, cur)

        return res