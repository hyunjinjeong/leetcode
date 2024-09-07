class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        chain = {}
        for word in sorted(words, key=lambda w: len(w)):
            chain[word] = 1
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]
                if prev_word in chain:
                    chain[word] = max(chain[prev_word] + 1, chain[word])
        
        return max(chain.values())