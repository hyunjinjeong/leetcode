class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # 길이마다 모든 순열의 수를 구하면 될 듯
        counter = collections.Counter(tiles)

        def dfs(pos, counter):
            if pos == len(tiles):
                return 0
            
            total = 0
            for c, count in counter.items():
                if count == 0:
                    continue

                total += 1 # c

                counter[c] -= 1
                total += dfs(pos + 1, counter)
                counter[c] += 1
            
            return total
        
        return dfs(0, counter)
