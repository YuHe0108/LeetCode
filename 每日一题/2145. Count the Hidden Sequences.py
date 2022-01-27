from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        max_dif = max(abs(max(differences)), abs(min(differences)))
        left = max_dif - lower
        right = upper - max_dif
        if right < left:
            return 0

        return
