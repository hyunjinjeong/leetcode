class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # 그래프는 아닌 것 같음...
        # 이미 알파벳인 도미노들은 제외해도 됨
        # 그러면 .들에 대해서만 계산하면 되는데
        # BFS 비슷하게 계산하면 되지 않으려나?
        # 근데 .으로 남는 도미노를 어떻게 계산하지..
        # q에서 두 번 나올테니까 set 같은데에 저장해두면 되겠다.
        
        domino_list = list(dominoes)

        q = collections.deque()
        for i in range(len(domino_list)):
            if domino_list[i] in ["L", "R"]:
                q.append(i)
        
        while q:
            seen = set()
            for _ in range(len(q)):
                i = q.popleft()
                if domino_list[i] == "L":
                    if i > 0 and domino_list[i - 1] == ".":
                        domino_list[i - 1] = "L"
                        q.append(i - 1)
                        seen.add(i - 1)
                    elif i - 1 in seen:
                        domino_list[i - 1] = "."
                elif domino_list[i] == "R":
                    if i < len(domino_list) - 1 and domino_list[i + 1] == ".":
                        domino_list[i + 1] = "R"
                        q.append(i + 1)
                        seen.add(i + 1)
                    elif i + 1 in seen:
                        domino_list[i + 1] = "."
        
        return "".join(domino_list)