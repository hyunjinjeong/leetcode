class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_to_name = {}
        for i in range(len(heights)):
            height_to_name[heights[i]] = names[i]
        
        heights.sort(reverse=True)
        return [height_to_name[h] for h in heights]