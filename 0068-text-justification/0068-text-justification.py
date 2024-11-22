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
            if curr_width == 0:
                curr_line.append(word)
                curr_width = len(word)
            else:
                if curr_width + len(word) + 1 <= maxWidth:
                    curr_line.append(word)
                    curr_width += len(word) + 1
                else:
                    word_count = len(curr_line)
                    if word_count == 1:
                        res.append(curr_line[0] + " " * (maxWidth - curr_width))
                    else:
                        curr_str = ""
                        spacing = maxWidth - curr_width + (word_count - 1)
                        each_spacing = spacing // (word_count - 1)
                        remainder = spacing % (word_count -1)
                        for w in curr_line:
                            curr_str += w
                            if spacing >= each_spacing:
                                curr_str += " " * each_spacing
                                spacing -= each_spacing
                                if remainder:
                                    curr_str += " "
                                    spacing -= 1
                                    remainder -= 1
                            else:
                                curr_str += " " * spacing
                                spacing = 0
                        res.append(curr_str)

                    curr_line = [word]
                    curr_width = len(word)
        
        curr_str = " ".join(curr_line)
        curr_str += " " * (maxWidth - len(curr_str))
        res.append(curr_str)
        
        return res