class Solution:
    def countValidWords(self, sentence: str) -> int:
        symbols = [',', '.', '!']
        words = sentence.split(' ') # 根据空格拆分
        cnt = 0
        for word in words:
            if len(word) == 0:
                continue
            if len(word) == 1 and word == '-':
                continue
            if len(word) == 1 and word in symbols:
                cnt += 1
                continue

            is_word = True
            line_cnt = 0
            alpha_cnt = 0
            n = len(word)
            for i, w in enumerate(word):
                if w.isalpha():
                    alpha_cnt += 1
                    continue
                elif i == n-1 and w in symbols:
                    continue
                elif 0 < i < n-1 and w == '-' and line_cnt == 0 and word[i+1].isalpha():
                    line_cnt += 1
                    continue
                else:
                    is_word = False
                    break
            if is_word and alpha_cnt > 0:
                cnt += 1
        return cnt