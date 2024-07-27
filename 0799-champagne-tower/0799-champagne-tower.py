class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # 파스칼의 삼각형.. 비슷한 거 같은데
        row = [poured]
        for _ in range(query_row):
            new_row = [0] * (len(row) + 1)
            for i in range(len(row)):
                pour = (row[i] - 1) / 2
                if pour > 0:
                    new_row[i] += pour
                    new_row[i + 1] += pour
            row = new_row
        
        return row[query_glass] if row[query_glass] < 1 else 1