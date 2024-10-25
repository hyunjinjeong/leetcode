class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # 이거.. 그 반대로 생각하는거 아닌가?
        # len(cardPoints) - k 길이의 subarray 합 중 minimum을 구해서 sum에서 빼는?
        N = len(cardPoints)
        all_sum = sum(cardPoints)

        rest_length = N - k
        if rest_length == 0:
            return all_sum

        rest_sum = 0
        min_rest_sum = all_sum

        for i in range(N):
            rest_sum += cardPoints[i]
            if i >= rest_length - 1:
                min_rest_sum = min(min_rest_sum, rest_sum)
                rest_sum -= cardPoints[i - rest_length + 1]
        
        return all_sum - min_rest_sum