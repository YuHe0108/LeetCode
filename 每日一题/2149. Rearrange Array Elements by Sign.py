class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        b_num = []
        s_num = []
        for v in nums:
            if v < 0:
                s_num.append(v)
            else:
                b_num.append(v)

        res = []
        while b_num and s_num:
            res.append(b_num.pop(0))
            res.append(s_num.pop(0))

        if b_num:
            res += b_num
        if s_num:
            res += s_num
        return res

