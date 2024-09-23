class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 항상 str1이 더 길도록
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        def check(k):
            if len(str1) % k != 0 or len(str2) % k != 0:
                return False
            
            n1, n2 = len(str1) // k, len(str2) // k
            prefix = str2[:k]

            return str1 == prefix * n1 and str2 == prefix * n2
            
        for i in range(len(str2), 0, -1):
            if check(i):
                return str2[:i]
        
        return ""