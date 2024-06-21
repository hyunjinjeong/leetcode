class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # stack을 쓰면 O(n) O(n)
        # 공간을 O(1)로 만들려면...
        def next_index(word, i):
            skip = 0
            while i >= 0:
                if skip == 0 and word[i] != "#":
                    break
                if word[i] == "#":
                    skip += 1
                else:
                    skip -= 1
                i -= 1
            return i
            
        i_s, i_t = len(s) - 1, len(t) - 1
        while i_s >= 0 or i_t >= 0:
            i_s = next_index(s, i_s)
            i_t = next_index(t, i_t)
            
            c_s = s[i_s] if i_s >= 0 else ""
            c_t = t[i_t] if i_t >= 0 else ""
            
            if c_s != c_t:
                return False
            
            i_s -= 1
            i_t -= 1
        
        return True