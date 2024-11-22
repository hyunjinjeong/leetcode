class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # greedy
        # curr_sum <= maxWidth가 될 때까지 더하다가
        # 넘는 순간 넣으면 될 듯. 근데 word 사이 space를 고려해야 함
        # This, is, an이면 8이지만 space를 고려하면 10.
        # maxWidth = 16이니까 6개의 남은 스페이스를 3개, 3개 공평하게 분배
        # 마지막 라인은 어떻게 처리하지?
        # curr_width가 maxWidth를 안 넘고 loop을 빠져 나오겠네
        
        res = []

        curr_width = 0
        curr_line = []
        for word in words:
            # Add a new line
            if curr_width + len(curr_line) + len(word) > maxWidth:
                extra_space = maxWidth - curr_width
                spacing = extra_space // max(1, len(curr_line) - 1)
                remainder = extra_space % max(1, len(curr_line) - 1)

                for i in range(max(1, len(curr_line) - 1)):
                    curr_line[i] += " " * spacing
                    if remainder:
                        curr_line[i] += " "
                        remainder -= 1
                
                res.append("".join(curr_line))
                curr_line = []
                curr_width = 0
            
            curr_line.append(word)
            curr_width += len(word)
        
        last_line = " ".join(curr_line)
        last_line += " " * (maxWidth - len(last_line))
        res.append(last_line)
        
        return res