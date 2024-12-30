class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        paid_bills = collections.defaultdict(int)
        
        for bill in bills:
            paid_bills[bill] += 1

            change = bill - 5 # could be 0, 5, 15
            if change == 5:
                paid_bills[5] -= 1
            if change == 15:
                paid_bills[5] -= 1
                paid_bills[10] -= 1
            
            if paid_bills[5] < 0 or paid_bills[10] < 0:
                return False
            
        return True