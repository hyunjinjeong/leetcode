class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # sticker마다 n개씩 뺄 수 있단 말이지..
        # 그런데 sticker와 target이 겹친다고 다 빼야하나? 그게 최적이 아닐 수도 있음
        # 아니지 각 캐릭터를 1개씩 쓸 수 있으니까 무조건 다 빼는게 이득인듯?
        # sticker를 돌면서 target에서 뺌
        # 중간상태를 재활용할 수 있으니까 DP로 갈 수 있을 것 같음
        # 근데 상태를 어떻게 정의하지?
        # lowercase alphabet이니까 배열에 적어두기?
        # hashmap으로 처리하기?
        # 26개짜리 tuple은 아닐...거 같은데

        @cache
        def dfs(i, curr_target):
            if curr_target == "":
                return 0
            if i == len(stickers):
                return float("inf")

            sticker = stickers[i]
            counter = sticker_counter[i]

            # not pick
            not_pick = dfs(i + 1, curr_target)
            
            # pick
            should_pick = False
            target_counter = collections.Counter(curr_target)
            for c in target_counter:
                if c in counter:
                    should_pick = True
                    target_counter[c] = max(target_counter[c] - counter[c], 0)
            
            new_word = ""
            for c in target_counter:
                new_word += c * target_counter[c]
            
            if should_pick:
                pick = 1 + dfs(i, new_word)
                return min(pick, not_pick)
            else:
                return not_pick
            
        sticker_counter = {}
        for i, sticker in enumerate(stickers):
            sticker_counter[i] = collections.Counter(sticker)

        res = dfs(0, target)
        return res if res != float("inf") else -1