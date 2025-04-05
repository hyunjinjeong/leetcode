class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = k
        black_count = 0

        left = 0
        for right in range(len(blocks)):
            if blocks[right] == "B":
                black_count += 1

            if right - left + 1 < k:
                continue
            
            res = min(k - black_count, res)

            if blocks[left] == "B":
                black_count -= 1
            left += 1

        return res