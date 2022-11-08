class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = strs[0]
        
        for string in strs:
            i = 0
            common = ""
            while i < len(answer) and i < len(string):
                if answer[i] != string[i]:
                    break
                common += answer[i]
                i += 1
            answer = common
            
        return answer