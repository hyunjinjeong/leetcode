class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # 리스트 순서대로 뽑는게 아니구나
        # 그럼 정렬을 먼저 하는게 좋을 것 같고...
        # 길이가 같으면 predecessor가 못 됨. 길이 차이가 1이여야만 가능
        # 그럼 predecessor를 빠르게 구하는 방법은 뭐가 있을까...
        # 각각 문자의 길이가 최대 16이니까 모두 구하는 방법도 있을 듯
        # 각 자리마다 최대 27개... 16*27개의 경우의 수인가?
        # 근데 처음부터 쭉 쌓는게 아니고.. 중간부터 시작되는 놈이 있을거란 말이지
        # 그러면 각 문자마다 최대 갯수를 저장해놓으면 될 듯
        # 아니면 해시맵을 활용할 수 있으려나
        # chain[word] = 1 이런 느낌으로..
        words.sort(key=lambda word: len(word))
        chain = {}
        for word in words:
            chain[word] = 1
            # 반대로 현재 문자에서 하나씩 빼도 되겠네...
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]
                if prev_word in chain:
                    chain[word] = max(chain[prev_word] + 1, chain[word])
        
        return max(chain.values())