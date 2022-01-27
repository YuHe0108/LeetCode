class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(' ')
        ans = 0
        for word in words:
            is_ok = True
            for a in word:
                if a in brokenLetters:
                    is_ok = False
                    break
            if is_ok:
                ans += 1
        return ans
