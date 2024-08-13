class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # 아까처럼 할 필요 없이 전체를 queue로 시뮬레이션 하면 되는구나
        deck.sort()
        
        q = collections.deque([i for i in range(len(deck))])

        res = [0] * len(deck)
        for card in deck:
            res[q.popleft()] = card
            if q:
                q.append(q.popleft())
        
        return res