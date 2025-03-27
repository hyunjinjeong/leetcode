class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # set을 만들어두고 2중 for문 돌면 됨. brute force.
        # 이걸 어떻게 최적화할까?
        # 첫번째 글자로 묶어보자
        ideas_by_first = [set() for _ in range(26)]
        for idea in ideas:
            ideas_by_first[ord(idea[0]) - ord("a")].add(idea[1:])

        res = 0
        for i in range(25):
            a = ideas_by_first[i]
            for j in range(i + 1, 26):
                b = ideas_by_first[j]
                
                shared = a & b
                res += 2 * (len(a) - len(shared)) * (len(b) - len(shared))
                
        return res