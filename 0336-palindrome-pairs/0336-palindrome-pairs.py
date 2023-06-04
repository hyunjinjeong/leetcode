class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_to_index = {word: i for i, word in enumerate(words)}
        ans = []
        
        for word, index in word_to_index.items():
            # 한 글자씩 slice해서 비교.
            for j in range(len(word)+1):
                prefix, suffix = word[:j], word[j:]
                
                if self.is_palindrome(prefix):
                    back = suffix[::-1]
                    # abandon -> "aba"인 경우. nodn + aba + ndon 식으로 붙이면 됨
                    # 따라서 suffix를 뒤집어서 확인.
                    if back != word and back in word_to_index:
                        ans.append([word_to_index[back], index])
                
                # suffix인 경우도 마찬가지로 확인.
                # prefix와 반대로 생각하면 됨...
                # 이 때 empty string은 중복 방지용으로 확인
                if suffix != "" and self.is_palindrome(suffix):
                    back = prefix[::-1]
                    if back != word and back in word_to_index:
                        ans.append([index, word_to_index[back]])
        
        return ans
    
    def is_palindrome(self, s):
        return s == s[::-1]