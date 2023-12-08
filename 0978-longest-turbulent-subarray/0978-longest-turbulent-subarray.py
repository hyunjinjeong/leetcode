class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # 일단 brute force는 2번 도니까 O(n^2)
        
#         ans = 0
#         for i in range(len(arr)):
#             before = None
#             last_j = i
#             for j in range(i+1, len(arr)):
#                 prev, curr = arr[j-1], arr[j]
#                 # before 초기화
#                 if before is None:
#                     if prev < curr:
#                         before = "gt"
#                         last_j = j
#                         continue
#                     elif prev > curr:
#                         before = "lt"
#                         last_j = j
#                         continue
#                     else:
#                         break
                
#                 if before == "gt" and prev > curr:
#                     before = "lt"
#                     last_j = j
#                 elif before == "lt" and prev < curr:
#                     before = "gt"
#                     last_j = j
#                 else:
#                     break
            
#             curr_len = last_j - i + 1
#             ans = max(curr_len, ans)
        
#         return ans
        
        # Kadane 알고리즘 쓸 수 있을 것 같기도..?
        ans = 1
        curr_len = 1
        
        op = None
        for i in range(1, len(arr)):
            prev, curr = arr[i-1], arr[i]
            
            if prev > curr:
                if op is None:
                    curr_len += 1
                elif op == "lt":
                    curr_len += 1 
                else:
                    curr_len = 2
                op = "gt"
            elif prev < curr:
                if op is None:
                    curr_len += 1
                elif op == "gt":
                    curr_len += 1
                else:
                    curr_len = 2
                op = "lt"
            else:
                curr_len = 1
                op = None
            
            ans = max(curr_len, ans)
        
        return ans