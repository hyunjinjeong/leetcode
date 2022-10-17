class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 매번 sort 하니까 TLE 뜸... hashmap 이용해서 sorted된 값을 넣으면 된다.
        dt = {}
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            
            if sorted_word in dt:
                dt[sorted_word].append(word)
            else:
                dt[sorted_word] = [word]
        
        return [anagrams for anagrams in dt.values()]

                    
                