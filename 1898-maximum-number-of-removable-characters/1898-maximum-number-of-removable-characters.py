class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        # 일단 array에서 subsequence인지 구하는 방법은?
        # 그러면 여기서 removable을 뺀 다음엔..?
        # k는 binary search로 구하면 됨
        def is_subsequence(k):
            p_index = 0
            for i, c in enumerate(s):
                if i in remove and remove[i] <= k:
                    continue
                
                if c == p[p_index]:
                    p_index += 1
                
                if p_index == len(p):
                    return True
            
            return False
        
        lo, hi = 0, len(removable)
        remove = {r: i for i, r in enumerate(removable)}
        while lo < hi:
            mid = (lo + hi) // 2
            
            if is_subsequence(mid):
                lo = mid + 1
            else:
                hi = mid
        
        return lo