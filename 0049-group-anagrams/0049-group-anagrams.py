class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sort each str then save it to hashmap

        res = []
        anagram_indexes = {}

        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string in anagram_indexes:
                res[anagram_indexes[sorted_string]].append(s)
            else:
                anagram_indexes[sorted_string] = len(res)
                res.append([s])

        return res