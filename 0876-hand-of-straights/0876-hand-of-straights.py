class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # greedy?
        # 일단 답이 안 되는 경우
        if len(hand) % groupSize != 0:
            return False
        # groupSize - 1만큼 연속된게 있는지 살펴본다..?
        # groupSize가 3인 경우, 1이 있으면 2, 3도 있어야 하고
        # 4가 있으면 5, 6도 있어야 하고..
        # counter를 쓰면 더 편하려나
        hand.sort()

        counter = collections.Counter(hand)
        while counter:
            deleted_count = 0
            for key in counter.keys():
                found = True
                for candidate in range(key, key + groupSize):
                    found = candidate in counter and found
                    if not found:
                        break
                
                if found:
                    for candidate in range(key, key + groupSize):
                        counter[candidate] -= 1
                        if counter[candidate] == 0:
                            del counter[candidate]
                        deleted_count += 1
                    break
            
            if deleted_count == 0:
                return False

        return True