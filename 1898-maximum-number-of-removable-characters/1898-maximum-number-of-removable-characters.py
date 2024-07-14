class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        # 일단 array에서 subsequence인지 구하는 방법은?
        # 그러면 여기서 removable을 뺀 다음엔..?
        # k는 binary search로 구하면 됨
        def is_subsequence(k):
            removable_set = set(removable[:k+1])

            p_index = 0
            for i, c in enumerate(s):
                if i in removable_set:
                    continue
                
                if c == p[p_index]:
                    p_index += 1
                
                if p_index == len(p):
                    return True
            
            return False
        
        # 0, 3, 1. 만족할거니까 2, 3, 2.
        # 2, 3, 2도 만족할 거임. 그러면 3 3이 되고
        # lo = 3인 상태로 탈출

        lo, hi = 0, len(removable)
        while lo < hi:
            mid = (lo + hi) // 2
            
            if is_subsequence(mid):
                lo = mid + 1
            else:
                hi = mid
        
        return lo