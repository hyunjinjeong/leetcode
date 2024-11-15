class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda item: item[1], reverse=True)
        
        res = 0

        for box_count, box_unit_count in boxTypes:
            if not truckSize:
                break
            boxes_to_use = min(box_count, truckSize)
            res += boxes_to_use * box_unit_count
            truckSize -= boxes_to_use
        
        return res
        