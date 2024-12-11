class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # 한번 close하면 다시 open하지는 않는 듯
        # 그러면 close할 곳이 N개 있고..
        # prefix sum 처럼 YES NO에 대한 배열을 각각 저장해서
        # yes[i - 1] + no[i]가 min이 되는 값을 찾으면 되지 않을까?
        # 예를 들어서
        # YYNY는
        # yes는 0 0 1 1
        # no는 3 2 1 1
        # 0은 3이고, 1은 2, 2도 1, 3은 2, 4는 1. 3 2 1 2 1.

        # NNNNN는
        # yes가 1 2 3 4 5
        # no는 0 0 0 0 0
        # 그래서 0 1 2 3 4 5 이런 식으로 되겠다.
        
        # # 근데 yes는 순서대로 세나가면 되니까 굳이 저장할 필요가 없네
        # # NO만 미리 계산해두면 될 듯?
        # N = len(customers)

        # close_penalty = [0] * (N + 1)
        # for i in range(N - 1, -1, -1):
        #     close_penalty[i] = close_penalty[i + 1]
        #     if customers[i] == "Y":
        #         close_penalty[i] += 1
        
        # curr_min = N
        # open_penalty = 0
        # res = -1
        # for i in range(N + 1):
        #     if open_penalty + close_penalty[i] < curr_min:
        #         curr_min = open_penalty + close_penalty[i]
        #         res = i

        #     if i < N and customers[i] == "N": # open penalty는 i - 1번쨰껄 계산해야 함
        #         open_penalty += 1

        # return res

        # one pass도 되네
        min_penalty = 0
        curr_penalty = 0
        res = 0

        for i, c in enumerate(customers):
            if c == "Y":
                curr_penalty -= 1
            else:
                curr_penalty += 1
        
            if curr_penalty < min_penalty:
                res = i + 1
                min_penalty = curr_penalty
        
        return res