class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        # 각 count마다 갯수를 저장해놓고
        # nC2 로 계산하면 되지 않나? 4C2 == 4 * 3 // 2 == 6
        counter = {}
        for width, height in rectangles:
            ratio = width / height
            counter[ratio] = counter.get(ratio, 0) + 1
        
        res = 0
        for count in counter.values():
            res += (count * (count - 1)) // 2
        
        return res