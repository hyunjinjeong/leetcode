class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        M, N = len(img), len(img[0])

        def calc(i, j):
            curr_sum = img[i][j]
            cnt = 1
            
            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                next_i, next_j = i + di, j + dj
                if 0 <= next_i < M and 0 <= next_j < N:
                    curr_sum += img[next_i][next_j]
                    cnt += 1
            
            return math.floor(curr_sum / cnt)

        
        res = [[0] * N for _ in range(M)]

        for i in range(M):
            for j in range(N):
                res[i][j] = calc(i, j)
        
        return res