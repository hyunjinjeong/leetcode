class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # 1 10 11 100 101이 있으면 1 100 101 10 11 순서인가?
        # 숫자가 위치할 곳을 미리 계산할 수 있는건가
        # 예를 들어 2는 1로 시작하는 모든 숫자 바로 뒤에 올거고
        # 11은? 10으로 시작하는 모든 숫자 바로 뒤에
        # 그럼 101은..? 100 다음인데

        def dfs(num):
            if num > n:
                return
            
            self.res.append(num)
            for digit in range(10):
                next_num = num * 10 + digit
                dfs(next_num)

        self.res = []
        for digit in range(1, 10):
            dfs(digit)
        
        return self.res
