class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentences = sentence.split(" ")

        for i in range(1, len(sentences) + 1):
            curr, prev = i % len(sentences), (i - 1) % len(sentences)
            if sentences[curr][0] != sentences[prev][-1]:
                return False
        return True
