class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # 모든 pair에 대해 gcd를 구해놔야 하나? 그러면 n^2 * log(max(num))이 된다.
        # 엣지를 만들고 전체 그래프가 모두 연결되어 있는지 보면 된다. union find. -> O(N^2)?
        # 그리고 N개를 돌면서 parent가 다른 친구가 있으면 false임
        # MLE ㅠㅠ
        # hint: 각 숫자마다 prime factor에 대한 리스트를 만들고 걔네랑만 연결하면 된다
        N = len(nums)

        uf = UnionFind(N)

        factor_index = {}
        for i, num in enumerate(nums):
            div = 2
            while div * div <= num:
                if num % div == 0:
                    if div in factor_index:
                        uf.union(i, factor_index[div])
                    else:
                        factor_index[div] = i
                    
                    while num % div == 0:
                        num //= div
                div += 1
                
            if num > 1:
                if num in factor_index:
                    uf.union(i, factor_index[num])
                else:
                    factor_index[num] = i
        
        return uf.count == 1


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.count = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        
        if self.size[px] < self.size[py]:
            self.parent[px] = py
            self.size[py] += self.size[px]
        else:
            self.parent[py] = px
            self.size[px] += self.size[py]
        
        self.count -= 1