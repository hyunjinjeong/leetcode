class Solution:
    def minSteps(self, n: int) -> int:
        # 3 = 1 + 1 + 1 or 2 + 1
        # 처음에는 copy밖에 못하니까..
        # 1 다음에는 무조건 2가 된다.
        # 그래서 3이면 다시 paste 해서 A copy -> A paste -> A paste.
        # 만약 4면? A copy -> A paste -> AA copy -> AA paste. 4개. 혹은 A copy -> A paste * 3 해도 4개.
        # 5면? A copy -> A paste * 4 하면 5개
        # 6이면? 6개짜리 있을거고, A copy -> A paste -> AA copy -> AA paste -> AA paste 하면 5개.
        # 이게 홀수개면 무조건 A만 copy할 수 있네.. AA가 되는 순간부터는 짝수가 됨
        # 8이면? A copy -> A paste -> AA copy -> AA paste -> AAAA copy -> AAAA paste. 6개.

        # 규칙을 생각해보자.. 현재 개수의 2배씩만 더할 수 있음.
        # 즉 6은 2 2 2 .. 8은 2 2 4 . 10은? 2 2 2 2 2 밖에 안 됨.
        # 12는? 2 2 2 6 이 된다.
        # 14는? 얘도 2 * 7이고, 16은? 2 2 4 8.
        # 그러면 숫자를 2로 나눴을 때 여전히 2의 배수인지가 중요하네
        # 6은 2로 나눴을 때 3이니까 아님. 그래서 2가 3개.
        # 8은 2로 나눴을 때 4. 그러면 ops(4) + 2가 된다.
        # 12는 6. ops(6) + 2.
        # 16은 8. ops(8) + 2.
        # 그럼 20은? ops(10) + 2... 요런 식이구만.

        # 6은? A copy -> A paste -> AA copy -> AA paste -> AA paste. 5개.
        # 10은? 6에다가 AA paste를 2번 더. 그럼 7개.

        if n == 1:
            return 0
        if n % 2 == 1:
            return n

        cache = {}
        def dfs(num):
            if num == 2:
                return 2 # A copy + A paste
            if num in cache:
                return num
            
            ops = 0
            if (num // 2) % 2 == 1:
                ops = 2 + num // 2
            else:
                ops = 2 + dfs(num // 2)

            cache[num] = ops
            return ops
        
        return dfs(n)
