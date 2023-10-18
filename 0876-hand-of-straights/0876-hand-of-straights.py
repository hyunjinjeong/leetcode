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
        
        # 여기 체크하는 로직을 이렇게 복잡하게 할 필요가 없었음
        # 매번 최솟값만 뽑으면 됨.

        i = 0
        while i < len(hand):
            card = hand[i]
            for candidate in range(card, card + groupSize):
                if candidate not in counter:
                    return False
                
                counter[candidate] -= 1
                if counter[candidate] == 0:
                    del counter[candidate]
                
            while i < len(hand) and hand[i] not in counter:
                i += 1
        
        return True

        # while counter:
        #     deleted_count = 0
        #     for key in counter.keys():
        #         found = True
        #         for candidate in range(key, key + groupSize):
        #             found = candidate in counter and found
        #             if not found:
        #                 break
                
        #         if found:
        #             for candidate in range(key, key + groupSize):
        #                 counter[candidate] -= 1
        #                 if counter[candidate] == 0:
        #                     del counter[candidate]
        #                 deleted_count += 1
        #             break
            
        #     if deleted_count == 0:
        #         return False

        # return True