class Solution:
    def hammingWeight(self, n: int) -> int:
#         count = 0
        
#         while n:
#             if n&1:
#                 count += 1
#             n = n >> 1
        
#         return count
        # 위에는 내가 생각한 방법인데..
        # n = n & n-1 을 이용하면 더 짧고 간단하게 할 수 있다.
        # n이 1100이라고 하면 n-1은 1011이라서 둘이 & 하면 1000 이런 식으로.
        # 가장 오른쪽의 1을 제거하게 됨!
        count = 0
        while n:
            n = n & n-1
            count += 1
        return count