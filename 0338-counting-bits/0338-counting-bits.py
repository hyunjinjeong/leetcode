class Solution:
    def countBits(self, n: int) -> List[int]:
#         def get_one_count(num):
#             count = 0
#             while num:
#                 num &= num-1
#                 count += 1
#             return count
        
#         result = []
#         for num in range(n+1):
#             result.append(get_one_count(num))
        
#         return result
    
        # DP도 되고.. bit도 되는데 bit도 DP 형태로 할 수 있음.
        # 일단 엣지 케이스.
        answer = [0]
        # 그 담에 계산
        for num in range(1, n+1):
            if num & 1:
                answer.append(answer[num >> 1] + 1)
            else:
                answer.append(answer[num >> 1])
        return answer