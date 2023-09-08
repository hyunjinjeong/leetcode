class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 어떻게든 그래프를 만들어놓고 BFS 돌리기?
        # beginWord에서 시작해서.. 1글자씩만 다른 친구들이 neighbor인데
        # 어떻게 구하지
        # 미리 만들어둘 필요가 없었다.
        # 알파벳 소문자로만 이루어져 있다는 조건을 이용.
        # 가능한 모든 문자열을 돌면서 테스트.. (그래봐야 26개. O(1)이니까.)
        
        # BFS
        # 이건 공간은 O(n)이고.. 시간은 O(nm*2?)
        # queue 도는게 일단 O(n)이고, for문이 O(26 * m * m). substring이 O(m)이니까.
        lower_cases = "abcdefghijklmnopqrstuvwxyz"
        
        word_set = set(wordList)
        q = collections.deque([(beginWord, 1)])
        while q:
            word, seq = q.popleft()
            if word == endWord:
                return seq
            
            for i in range(len(word)):
                for c in lower_cases:
                    candidate = word[:i] + c + word[i+1:]
                    if candidate in word_set:
                        q.append((candidate, seq+1))
                        word_set.remove(candidate)

        return 0