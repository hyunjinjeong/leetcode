class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # 순열을 구해서 확인할 수도 있지만... counter 만들어서 투 포인터 쓴다면..?
        s1_counter = collections.Counter(s1)
        s2_counter = collections.Counter(s2[:len(s1)-1])

        for right in range(len(s1)-1, len(s2)):
            s2_counter[s2[right]] += 1

            if s1_counter == s2_counter:
                return True
            
            left = right - len(s1) + 1
            s2_counter[s2[left]] -= 1

        return False