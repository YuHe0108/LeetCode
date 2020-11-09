# DP解题思路

###### 1、174. Dungeon Game

###### 		从右下角开始向上遍历，原始的dp数组初始化为0 ，表示所有的位置至少有一滴血。

​		   (1) 如果 row = rows-1, 即左边界的时候，只能向上走， col = cols-1, 只能往左走。

​		  (2) 其他时候，两个方向都可以。

```python
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
    	rows, cols = len(dungeon), len(dungeon[0])
        dp = [[1] * cols for _ in range(rows)]
        for i in range(rows-1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i == rows - 1 and j == cols - 1:
                    dp[i][j] = 1
                elif i == rows - 1:
                    dp[i][j] = dp[i+1][j] - dungeon[i+1][j]
                elif j == cols - 1:
                    dp[i][j] = dp[i][j+1] - dungeon[i][j+1]
                else:
                    dp[i][j] = min(dp[i][j+1] - dungeon[i][j+1], dp[i+1][j] - 
                                   dungeon[i+1][j])
                dp[i][j] = max(dp[i][j], 1)
         dp[0][0] -= dungeon[0][0]
         dp[0][0] = max(dp[0][0], 1)
         return dp[0][0]
```

![174](E:\Codes\LeetCode\Dynamic Programming\0930\174.jpg)



#### 2、第二类区间型DP

<img src="C:\Users\Ying\AppData\Roaming\Typora\typora-user-images\image-20201005091947863.png" alt="image-20201005091947863" style="zoom:80%;" />



# 二、重点题型

##### 1320-Minimum Distance to Type a Word Using Two Fingers

```python
class Solution:
    def minimumDistance(self, word: str) -> int:
        def get_dist(A, B):
            a_x, a_y = A // 6, A % 6
            b_x, b_y = B // 6, B % 6
            return abs(a_x - b_x) + abs(a_y - b_y)

        n = len(word)
        dp = [[float('inf')]  * 26 for _ in range(n)]
        dp[0][:] = [0] * 26
        
        for k in range(1, n):
            cur = ord(word[k]) - ord('A')
            pre = ord(word[k-1]) - ord('A')
            for i in range(26):
                dp[k][i] = min(dp[k][i], 
                               dp[k-1][i] + get_dist(pre, cur), 
                               dp[k-1][cur] + get_dist(pre, i))
        return min(dp[-1][:])
```



#### 2、查找矩阵中的sub_matrix

##### 1074-Number of Submatrices That Sum to Target

```python
from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix, target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        def calc(arr):
            cnt = 0
            presum = 0
            record = defaultdict(int)
            record[0] = 1
            for i in range(cols):
                presum += arr[i]
                if presum - target in record:
                    cnt += record[presum - target]
                record[presum] += 1
            return cnt
        
        count = 0
        for i in range(rows):
            temp = [0] * cols
            for j in range(i, rows):
                for k in range(cols):
                    temp[k] += matrix[j][k]
                # 寻找sub_matrix == target的值
                count += calc(temp)
        return count
```

