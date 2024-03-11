class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []

        for op in operations:
            if self.is_int(op):
                records.append(int(op))
            elif op == "C":
                records.pop()
            elif op == "+":
                records.append(records[-1] + records[-2])
            else: # D
                records.append(records[-1] * 2)

        return sum(records)
    
    def is_int(self, s):
        try:
            int(s)
            return True
        except:
            return False