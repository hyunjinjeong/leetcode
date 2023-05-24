class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # dict에 일단 저장해서 BFS를 돌린다..?
        # 저장하는 형식은 어떻게 하지
        # 일단 1글자만 다른 것들을 찾을 수 있어야 하는데...
        # hot이라고 치면 hot: [dot, lot] 이런 식.
        
        # 먼저 hash table을 저장하고 하니까 O(n^2 * m)이고.. TLE 뜸
        # 미리 만들어둘 필요가 없었다.
        # 알파벳 소문자로만 이루어져 있다는 조건을 이용.
        # 가능한 모든 문자열을 돌면서 테스트.. (그래봐야 26개. O(1)이니까.)
        
        # BFS
        lower_cases = "abcdefghijklmnopqrstuvwxyz"
        
        word_set = set(wordList)
        q = collections.deque([(beginWord, 1)])
        visited = set(beginWord)
        while q:
            word, seq = q.popleft()
            if word == endWord:
                return seq
            
            for i in range(len(word)):
                for c in lower_cases:
                    candidate = word[:i] + c + word[i+1:]
                    if candidate not in visited and candidate in word_set:
                        q.append((candidate, seq+1))
                        visited.add(candidate)

        return 0
                