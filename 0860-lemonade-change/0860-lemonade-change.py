class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        paid_bills = collections.defaultdict(int)
        
        for bill in bills:
            paid_bills[bill] += 1

            change = bill - 5 # could be 0, 5, 15
            # 아 15일 땐 5 * 3으로도 계산할 수 있음.
            if change == 5:
                paid_bills[5] -= 1
            if change == 15:
                if paid_bills[10]:
                    paid_bills[10] -= 1
                    paid_bills[5] -= 1
                else:
                    paid_bills[5] -= 3
            
            if paid_bills[5] < 0 or paid_bills[10] < 0:
                return False
            
        return True