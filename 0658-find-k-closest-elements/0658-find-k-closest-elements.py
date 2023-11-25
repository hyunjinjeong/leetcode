class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         # -2 -1 0 1 2 이렇게 있을 수도 있음.
#         # 그러면 0을 찾는다고 하면
#         # 0에서 가까운거 4개면 -2 -1 0 1 인데
#         # binary search로 찾아서 two pointer? deque 쓰면 되고
        
#         def bisect():
#             lo, hi = 0, len(arr)
            
#             while lo < hi:
#                 mid = (lo + hi) // 2
                
#                 if arr[mid] < x:
#                     lo = mid + 1
#                 else:
#                     hi = mid
            
#             return lo
        
#         pos = bisect()
#         ans = collections.deque()
        
#         l, r = pos - 1, pos
#         while len(ans) < k:
#             if r >= len(arr):
#                 ans.appendleft(arr[l])
#                 l -= 1
#             elif l < 0:
#                 ans.append(arr[r])
#                 r += 1
#             else:
#                 # 비교 필요
#                 left, right = arr[l], arr[r]
#                 if abs(left - x) <= abs(right - x):
#                     ans.appendleft(arr[l])
#                     l -= 1
#                 else:
#                     ans.append(arr[r])
#                     r += 1
            
#         return ans

        # boundary를 찾는 bisect 도 있당
        lo, hi = 0, len(arr) - k
        while lo < hi:
            mid = (lo + hi) // 2
            if x - arr[mid] > arr[mid + k] - x:
                lo = mid + 1
            else:
                hi = mid
            
        return arr[lo:lo + k]