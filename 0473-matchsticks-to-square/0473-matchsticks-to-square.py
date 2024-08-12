class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # 이거는.. 합이 4로 나눠지면 되나..? 는 예제 2번에서 걸림
        # 일단 4로 나눠지지 않으면 false는 맞음. 그리고 4로 나눈 값이 각 변의 길이이고
        # 그러면 k1, k2, k3, k4개씩을 사용해서 sum // 4가 되는 수가 있으면 됨
        # sum // 4보다 큰 스틱이 있어도 안 되는 거고..
        # 길이가 최대 15니까 backtracking으로 전수조사하면 되려나?
        def backtrack(i, lengths):
            if i == len(matchsticks):
                return all(length == target_length for length in lengths)
            
            for j in range(4):
                if matchsticks[i] + lengths[j] <= target_length:
                    lengths[j] += matchsticks[i]
                    if backtrack(i+1, lengths):
                        return True
                    lengths[j] -= matchsticks[i]
            return False

        sum_sticks = sum(matchsticks)
        if sum_sticks % 4 != 0:
            return False
        
        matchsticks.sort(reverse=True) # 정답은 맞았는데... sort를 안하니까 TLE가 뜨네
        target_length = sum_sticks // 4
        return backtrack(0, [0, 0, 0, 0])