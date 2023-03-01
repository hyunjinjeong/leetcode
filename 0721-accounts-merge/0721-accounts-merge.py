class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 그래프 문제로 치환할 수 있음... connected components를 찾는 것
        # 이메일 -> 계정으로 hashmap 저장한 다음에 DFS로 도는 방법
        emails_accounts_map = {}
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                if email in emails_accounts_map:
                    emails_accounts_map[email].append(i)
                else:
                    emails_accounts_map[email] = [i]

        visited_accounts = [False] * len(accounts)
        def dfs(i, emails):
            if visited_accounts[i]:
                return
            visited_accounts[i] = True
            
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in emails_accounts_map[email]:
                    dfs(neighbor, emails)
        
        res = []
        for i, account in enumerate(accounts):
            if visited_accounts[i]:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
            
        return res