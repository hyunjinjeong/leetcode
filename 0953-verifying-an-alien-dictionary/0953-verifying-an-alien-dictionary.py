class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 그냥 이렇게 처음부터 다 돌아도 되는구나
        # 캐릭터가 같을 때만 뒤를 비교하면 됨
        order_map = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for j in range(len(word1)):
                if j == len(word2):
                    return False

                c1_score, c2_score = order_map[word1[j]], order_map[word2[j]]
                if c1_score > c2_score:
                    return False
                elif c1_score < c2_score:
                    break

        return True