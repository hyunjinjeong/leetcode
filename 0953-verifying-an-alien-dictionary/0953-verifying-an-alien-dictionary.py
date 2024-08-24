class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # hmm.. 그냥 다 돌아보면 되나?
        # order를 각각 점수라고 생각해서..
        # string을 int로 치환해서 해볼까?
        # abc -> 123점 같은 식.
        # 이렇게 하려면 가장 긴 스트링 길이만큼 *10을 해줘야 하는구나
        score = {}
        for i, c in enumerate(order):
            score[c] = i + 1
        
        longest_length = 0
        for word in words:
            longest_length = max(longest_length, len(word))
        
        word_scores = []
        for word in words:
            curr = 0
            for c in word:
                curr = score[c] + curr * 10
            for _ in range(longest_length - len(word)):
                curr *= 10
            word_scores.append(curr)
    
        prev_score = 0
        for word_score in word_scores:
            if word_score < prev_score:
                return False
            prev_score = word_score
        return True