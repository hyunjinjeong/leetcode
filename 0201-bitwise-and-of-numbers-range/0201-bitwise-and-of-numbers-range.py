class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 1번씩 다 도는건 아닐 거 같고..
        # bitwise의 성질을 이용한다?
        # common prefix를 구하면 되는구나
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift