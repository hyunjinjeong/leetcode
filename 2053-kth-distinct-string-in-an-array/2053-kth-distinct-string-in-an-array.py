class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = collections.Counter(arr)
        
        n = 1
        for s in arr:
            if counter[s] == 1:
                if n == k:
                    return s
                n += 1
        
        return ""