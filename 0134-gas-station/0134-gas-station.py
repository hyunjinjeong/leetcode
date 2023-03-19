class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         # 일단 naive로 하면?
#         # 0부터 시작해서 0까지 돌아오는 것. -> 1 to 1 -> ... 이렇게 해보면 됨.
#         # 이렇게 하면 시간 복잡도는 n^2
#         # 이건 TLE 뜸.
#         for start in range(len(gas)):
#             cnt = 0
#             curr_gas = 0
#             while cnt < len(gas):
#                 dest = (start + cnt) % len(gas)
#                 curr_gas += gas[dest]
#                 curr_gas -= cost[dest]
                
#                 if curr_gas < 0:
#                     break
                    
#                 cnt += 1
            
#             if curr_gas >= 0:
#                 return start
        
#         return -1
        # 뭔가 DP로 최적화할 수 있을 것 같다. 근데 시작지점에 따라 값이 변해서... 최적 부분 문제를 어떻게 찾지
        # ? 그리디였음..
        # total gas > total cost면 정답이 존재. 없으면 -1
        # 그 다음에는 시작 지점만 찾으면 됨.
        
        total_surplus = 0
        for i in range(len(gas)):
            total_surplus += gas[i] - cost[i]
        if total_surplus < 0:
            return -1
        
        start, surplus = 0, 0
        for i in range(len(gas)):
            # 부분합이 0보다 작아지면 그 사이는 모두 답이 안 됨.
            # 뭔가 직관적으로 보이는데... 증명은 어케하지?
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i+1
                
        return start