class Solution:
    def splitString(self, s: str) -> bool:
        # 내림차순으로 나눠야 함. 그리고 int로 바꿨을 때 1씩 줄어야 하고.
        # 1234면 안되고 4321은 되고 그런거네
        # 050 49 요런것도 되고
        # 0050 049 요런것도 되고
        # 최대 길이가 20인거 보면 backtracking인가?

        # 200100은 어떻게 true가 되는거지;
        # 2 / 001 / 00 이구나

        # i가 0일 때
        # start:1, prev:2로 dfs 진입하고
        # 그럼 for문은 for i in range(1, 6)이고..
        # curr = int(s[1:i + 1])인데
        # i가 3일 때 curr = int(s[1:4]) = 1이 되면서,
        # start: 4, prev: 1으로 dfs 진입
        # 아 여기서 0이라서 start = 5일 때 바로 dfs 진입해서 False가 뜨는 구나
        # 그러면 trailing zero에 대한 처리를 별도로 해줘야 한다.
        # prev가 1일 때는 dfs를 바로 len(s)까지 가야할 듯?

        def dfs(start, prev):
            if start == len(s):
                return True
            
            if prev == 1:
                curr = int(s[start:])
                return prev - curr == 1
            
            for i in range(start, len(s)):
                curr = int(s[start:i + 1])
                if prev - curr == 1:
                    return dfs(i + 1, curr)
            
            return False
        
        for i in range(len(s) - 1):
            val = int(s[:i + 1])
            if dfs(i + 1, val):
                return True
        
        return False