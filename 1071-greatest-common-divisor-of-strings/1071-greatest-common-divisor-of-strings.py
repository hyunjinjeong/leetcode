class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 항상 str1이 더 길도록
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        def check(s1, s2):
            if len(s1) % len(s2) != 0:
                return False
            
            for i in range(0, len(s1), len(s2)):
                for j in range(len(s2)):
                    if s1[i + j] != s2[j]:
                        return False
            
            return True
        
        for i in range(len(str2) - 1, -1, -1):
            if len(str2) % (i + 1) == 0 and check(str2, str2[:i+1]) and check(str1, str2[:i+1]):
                return str2[:i+1]
        
        return ""