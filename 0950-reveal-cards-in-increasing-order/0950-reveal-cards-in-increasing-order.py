class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # 0번째를 reveal하면 1번째는 맨 뒤로 가고.. 이걸 반복해서 reveal한 순서가 오름차순이어야 함
        # 일단 0번째는 min()이 되어야 하고
        # 짝수 인덱스에 있는 카드들은 오름차순이 되어야 함. 요건 전체 갯수가 홀수이든 짝수이든 동일..
        # 문제는 홀수 인덱스에 있는 친구들인데.. 
        # 1, 3, 5, 7 ... 이라고 하면
        # 3에 그다음 낮은 수가 들어가야 하고, 그다음은 7, 이런 식으로 두칸씩 건너뜀
        
        deck.sort()
        deck_index = 0
        ans = [0] * len(deck)

        for i in range(0, len(deck), 2):
            ans[i] = deck[deck_index]
            deck_index += 1
        
        # 홀수는 뭐 queue 만들어서 하나씩 넣으면 되지 않을까...
        odds = collections.deque([i for i in range(1, len(deck), 2)])
        # 전체 갯수가 짝수개면 맨 뒤에 하나 있으니까.. 앞으로 땡겨줘야 함
        if len(deck) % 2 == 0:
            odds.appendleft(odds.pop())
        while odds:
            # 하나 건너뛰고
            odds.append(odds.popleft())
            ans[odds.popleft()] = deck[deck_index]
            deck_index += 1
        
        return ans