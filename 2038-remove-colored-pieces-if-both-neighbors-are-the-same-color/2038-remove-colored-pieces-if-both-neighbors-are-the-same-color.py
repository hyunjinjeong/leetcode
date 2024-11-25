class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # 몇 개를 지울 수 있는지 세면 되는거 아닌가?
        # AAA... 이렇게 연속해서 있는 경우 N - 2개만큼을 지울 수 있음
        # 그러면 alice < bob이면 bob이 이기는 거고
        # alice > bob이면 alice가 이기는 거고
        # 같을 때는 AAABBB -> AABBB -> AABB -> Alice loses. 즉 alice <= bob일 때 bob이 이김

        alice_removable_count, bob_removable_count = 0, 0

        curr_letter, curr_streak = colors[0], 1
        for i in range(1, len(colors)):
            if colors[i] == curr_letter:
                curr_streak += 1
                if curr_streak >= 3:
                    if curr_letter == "A":
                        alice_removable_count += 1
                    else:
                        bob_removable_count += 1
            else:
                curr_letter = colors[i]
                curr_streak = 1
        
        return alice_removable_count > bob_removable_count