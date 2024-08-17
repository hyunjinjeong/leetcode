class Solution:
    def makeGood(self, s: str) -> str:
        # s 길이가 최대 100이니까.. 그냥 시뮬레이션 돌리면 되나?
        # 어떻게 하지..? 일단 s를 array로 만들어?
        # 그러면 중간에 날리는게 O(n)인데.. string도 마찬가지고
        for i in range(len(s) - 1):
            if s[i].lower() == s[i + 1].lower() and s[i] != s[i + 1]:
                return self.makeGood(s[:i] + s[i+2:])
        
        return s