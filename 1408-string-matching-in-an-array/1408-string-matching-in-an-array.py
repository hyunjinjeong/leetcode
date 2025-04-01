class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        for i in range(len(words)):
            target = words[i]
            found = False
            for j in range(len(words)):
                if i == j:
                    continue
                
                comp = words[j]
                if len(target) > len(comp):
                    continue
                
                for k in range(len(comp) - len(target) + 1):
                    split_comp = comp[k:k + len(target)]
                    if target == split_comp:
                        res.append(target)
                        found = True
                        break
                
                if found:
                    break
        
        return res