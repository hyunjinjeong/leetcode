class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # grouping은 어떻게 하지..?
        # hash table 써서 정렬한 str을 key로 하면 되지 않을까
        dt = {}
        for string in strs:
            key = "".join(sorted(string))
            if key in dt:
                dt[key].append(string)
            else:
                dt[key] = [string]
        
        return dt.values()
