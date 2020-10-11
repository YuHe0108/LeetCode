###### 1456：

######     给定字符串s和整数k， 返回长度为k的s的任何子字符串中的最大元音字母数。英文的元音字母为（a，e，i，o，u）。


```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        alpha = {'a', 'e', 'i', 'o', 'u'}
        out, ans = 0, 0
        
        # 前 i 个字母是元音字母的是哪几个
        for i in range(k):
            if s[i] in alpha:
                ans += 1
        out = ans
        for i in range(k, len(s)):
            if s[i] in alpha:
                ans += 1
            if s[i-k] in alpha:
                ans -= 1
            out = max(out, ans)
        return out
```

