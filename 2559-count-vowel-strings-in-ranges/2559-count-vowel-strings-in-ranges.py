class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # prefix sum 이겠네
        VOWELS = set(["a", "e", "i", "o", "u"])

        prefix_sum = [0]
        for word in words:
            curr = 1 if word[0] in VOWELS and word[-1] in VOWELS else 0
            prefix_sum.append(prefix_sum[-1] + curr)
        
        # 0 1 1 2 3 4
        res = [0] * len(queries)
        for i, (l, r) in enumerate(queries):
            res[i] = prefix_sum[r + 1] - prefix_sum[l]
        
        return res
