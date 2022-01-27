class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        for num in range(n+1, pow(10, 7) + 1):
            count = defaultdict(int)
            for v in str(num):
                count[v] += 1
            is_res = True
            for k, v in count.items():
                if int(k) != v:
                    is_res = False
                    break
            if is_res:
                return num
            else:
                continue