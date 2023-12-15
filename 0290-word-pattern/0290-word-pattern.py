class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        pattern_map, word_map = {}, {}
        for i in range(len(words)):
            word, c = words[i], pattern[i]
            
            if word not in word_map:
                if c in pattern_map:
                    return False
                word_map[word] = c
                pattern_map[c] = word
            else:
                if word_map[word] != c:
                    return False
        
        return True