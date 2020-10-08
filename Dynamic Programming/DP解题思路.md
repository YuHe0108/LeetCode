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





