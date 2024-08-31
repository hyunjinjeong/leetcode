class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 이건 누가 봐도 backtracking
        def is_valid(s):
            num = int(s)
            if not 0 <= num <= 255:
                return False
            if len(s) >= 2 and s[0] == "0":
                return False
            return True

        def backtrack(left, curr, num_dots):
            if left == len(s) and num_dots == 4:
                self.res.append(curr[:-1]) # trailing dot 제거
                return
            
            for right in range(left, min(left + 3, len(s))):
                if is_valid(s[left:right+1]) and num_dots < 4:
                    backtrack(right + 1, curr + s[left:right+1] + ".", num_dots + 1)

        self.res = []
        if not 4 <= len(s) <= 12:
            return []
        
        backtrack(0, "", 0)
        return self.res