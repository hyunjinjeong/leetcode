class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 허허.. 식으로 풀 수도 있다.
        # 결국 시간은 max frequency를 가진 task에 의해 결정됨.
        # 마지막에는 max frequency를 가진 task의 갯수와 같고...
        freq = Counter(tasks)
        freq_values = freq.values()
        
        max_freq = max(freq_values)
        freq = list(freq_values)
        last_row = freq.count(max_freq)
        
        ans = (max_freq - 1) * (n + 1) + last_row
        return max(len(tasks), ans)
        
#         counter = collections.Counter(tasks)
        
#         # 갯수가 많은 task 순서대로 사이클 돌리면서 greedy하게 빼내야 되나 보다.
#         # 그러면 갯수가 많은 task 순서대로 n+1개 뽑기 <- 이걸 해야 하는데
#         # counter.most_common을 써서 일단 해보자.
        
#         ans = 0
#         while True:
#             most_common_tasks = counter.most_common(n+1)
#             len_most_common_tasks = len(most_common_tasks)
#             for task, _count in most_common_tasks:
#                 counter[task] -= 1
#                 ans += 1
#                 if counter[task] == 0:
#                     del counter[task]
            
#             if not counter:
#                 return ans
                
#             if len_most_common_tasks < n+1:
#                 ans += n+1 - len_most_common_tasks