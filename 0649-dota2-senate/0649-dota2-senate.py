class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # 이것도 greedy 같은데
        r_count, d_count = 0, 0
        for c in senate:
            if c == "R":
                r_count += 1
            else:
                d_count += 1

        q = collections.deque(senate)

        curr = senate[0]
        curr_count = 0
        while r_count and d_count:
            c = q.popleft()

            if curr_count == 0 or c == curr:
                curr = c
                q.append(c)
                curr_count += 1
            elif curr_count > 0:
                if c == "R":
                    r_count -= 1
                else:
                    d_count -= 1
                curr_count -= 1
        
        return "Radiant" if r_count else "Dire"