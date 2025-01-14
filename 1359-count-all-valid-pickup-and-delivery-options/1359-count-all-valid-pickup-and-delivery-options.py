class Solution:
    def countOrders(self, n: int) -> int:
        # order가 n개 있으면 모든 i에 대해 pi -> di 순서를 만족해야 함. 모든 시퀀스 갯수를 구하기.
        # [p1, d1]이 있을 때 p2, d2가 어디에 들어갈지를 정해야 함
        # [0, p1, 1, d1, 2]라고 하면
        # 위치가 3개.
        # 0에 p2를 넣는 경우 -> d2는 0, 1, 2에 넣을 수 있음. 3가지
        # 1에 p2를 넣는 경우 -> d2는 1, 2에 넣을 수 있음. 2가지
        # 2에 p2를 넣는 경우 -> d2는 2에 넣을 수 있음. 1가지

        # 뭔가 식을 세울 수 있을 것 같은데..
        # 다음으로 2개일 때는
        # [0, p1, 1, p2, 2, p3, 3, p4, 4]
        # 위치가 5개.
        # 0에 넣으면 6, 1에 넣으면 5, ... 해서 5에 넣으면 1까지
        # 1 + 2 + 3 + 4 + 5 = 5 * 6 // 2 = 15. 이전에 valid한 조합이 6개였으니 15 * 9 = 90. 이런 식이네

        # i번째일 때 넣을 수 있는 위치 갯수는 2 * (i - 1) + 1임. 이걸 n_p라고 하면
        # i일 때의 값은 prev * (n_p * (n_p + 1) // 2).
        MOD = 10 ** 9 + 7

        res = 1
        for i in range(1, n + 1):
            total_position = 2 * (i - 1) + 1
            possible_sequence = total_position * (total_position + 1) // 2
            res = (res * possible_sequence) % MOD
        
        return res