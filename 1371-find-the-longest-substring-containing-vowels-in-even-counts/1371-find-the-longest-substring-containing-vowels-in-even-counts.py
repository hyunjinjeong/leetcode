class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # sliding window를 한다고 할 때 어떻게 늘리고 줄이지?
        # prefix sum 같은걸 쓸 수 있으려나?
        # bitmask 문제였음; 어렵구만..
        def get_index(c):
            return ord(c) - ord("a")

        prefix_xor = 0

        character_map = [0] * 26
        # 00001, 00010, ...
        character_map[get_index("a")] = 1
        character_map[get_index("e")] = 2
        character_map[get_index("i")] = 4
        character_map[get_index("o")] = 8
        character_map[get_index("u")] = 16

        first_seen = [-1] * 32
        res = 0
        for i, c in enumerate(s):
            prefix_xor ^= character_map[get_index(c)]
            if first_seen[prefix_xor] == -1 and prefix_xor != 0:
                first_seen[prefix_xor] = i
            # prefix_xor 값이 같으면 두 구간 사이의 모든 모음의 수가 짝수임.
            res = max(res, i - first_seen[prefix_xor])
        
        return res
