class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0

        num = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha():
                i += num
                num = 0

                if i >= len(word):
                    return False
                if word[i] != abbr[j]:
                    return False

                i += 1
                j += 1
            else:
                if num == 0 and abbr[j] == "0":
                    return False
                num = num * 10 + int(abbr[j])
                j += 1
        
        i += num
        return i == len(word) and j == len(abbr)
