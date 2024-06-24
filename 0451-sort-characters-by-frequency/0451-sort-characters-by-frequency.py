class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1

        ans = []
        for c, count in sorted(freq.items(), reverse=True, key=lambda x: x[1]):
            for _ in range(count):
                ans.append(c)

        return "".join(ans)