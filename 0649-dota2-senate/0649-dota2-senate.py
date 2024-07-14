class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # 이것도 greedy 같은데
        # 각각 전체 count를 센 뒤에
        # loop 돌면서 상대 count를 깎아보면 될 듯?
        # RRDD
        # 2 -2
        # RRDDD
        # 2 -2 => 2 0 => 1 1
        # 이건 아니넹

        r_count, d_count = 0, 0
        for c in senate:
            if c == "R":
                r_count += 1
                if r_count > 0:
                    d_count -= 1
            elif c == "D":
                d_count += 1
                if d_count > 0:
                    r_count -= 1
        
        if r_count > d_count:
            return "Radiant"
        if r_count < d_count:
            return "Dire"
        
        # 같으면 먼저 나온게...
        return "Radiant" if senate[0] == "R" else "Dire"
        
        # for c in senate:
        #     if c == "R":
        #         d_count -= 1
        #     elif c == "D":
        #         r_count -= 1
            
        #     if d_count == 0:
        #         return "Radiant"
        #     if r_count == 0:
        #         return "Dire"