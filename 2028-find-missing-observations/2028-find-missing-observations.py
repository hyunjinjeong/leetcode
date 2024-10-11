class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # 일단 m과 n은 나와 있고, mean은 sum(total) // (m + n)인데
        # sum(total) = m_sum + n_sum이라고 할 때 n_sum을 구할 수 있음
        # 그러면 문제가 합이 n_sum인 1-6 사이의 숫자 n개의 배열을 만드는 것.
        m = len(rolls)
        m_sum = sum(rolls)
        n_sum = mean * (m + n) - m_sum

        if n_sum > 6 * n or n_sum < 1 * n: # impossible
            return []
        
        # n_sum을 n으로 나누면 평균값이 나옴. 그걸로 n개를 모두 채운 다음에
        # remainder를 여기저기 더해주면 되지 않을까?
        n_mean, n_remainder = n_sum // n, n_sum % n
        res = [n_mean] * n

        for i in range(n):
            if n_remainder == 0:
                break
            
            margin = min(n_remainder, 6 - res[i])
            res[i] += margin
            n_remainder -= margin

        return res