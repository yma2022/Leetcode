# Dynamic programming note

## What is dynamic programming?

Dynamic Programming (DP) is a programming paradigm that can systematically and efficiently explore all possible solutions to a problem. As such, it is capable of solving a wide variety of problems that often have the following characteristics:

1. The problem can be broken down into "overlapping subproblems" - smaller versions of the original problem that are re-used multiple times.
2. The problem has an "optimal substructure" - an optimal solution can be formed from optimal solutions to the overlapping subproblems of the original problem.

One well-known example of the appplication of dynamic programming is on Fibonacci sequence. If you wanted to find the Fibonacci number F(n), you can break it down into smaller subproblems - find F(n−1) and F(n−2) instead. Then, adding the solutions to these subproblems together gives the answer to the original question, F(n−1)+F(n−2)=F(n), which means the problem has optimal substructure, since a solution F(n) to the original problem can be formed from the solutions to the subproblems. These subproblems are also overlapping - for example, we would need F(4) to calculate both F(5) and F(6).

## Solve Fibonacci with DP

### Top-down

Top-down is implemented with recursion and made efficient with memoization.

```
// Pseudocode example for top-down

memo = hashmap
Function F(integer i):
    if i is 0 or 1: 
        return i
    if i doesn't exist in memo:
        memo[i] = F(i - 1) + F(i - 2)
    return memo[i]
```

Here the memoization is the hashmap which record calculated nodes to avoid repetive calculation. Top-down method starts with the last calculation at the top and recursively call the function to reach the answer.

### Bottome-up

Bottom-up is implemented with iteration and starts at the base cases. 

```
// Pseudocode example for bottom-up

F = array of length (n + 1)
F[0] = 0
F[1] = 1
for i from 2 to n:
    F[i] = F[i - 1] + F[i - 2]
```

Different from top-down method, bottom-up method starts the calculation from the bottom base cases and continue the calculation iteratively until reach the answer.

## Typical DP problems

### House robbery

#### LC 213. House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

```
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        result1 = self.robRange(nums, 0, len(nums) - 2)  # 情况二
        result2 = self.robRange(nums, 1, len(nums) - 1)  # 情况三
        return max(result1, result2)
    # 198.打家劫舍的逻辑
    def robRange(self, nums: List[int], start: int, end: int) -> int:
        if end == start:
            return nums[start]
        
        prev_max = nums[start]
        curr_max = max(nums[start], nums[start + 1])
        
        for i in range(start + 2, end + 1):
            temp = curr_max
            curr_max = max(prev_max + nums[i], curr_max)
            prev_max = temp
        
        return curr_max
```

### Kanpsack problem

#### 0-1 knapsack 
for the 0-1 knapsack problem, there is only 1 of each item. The core segment code to solve the problem with bottom-up method is:

```
for(int i = 0; i < weight.size(); i++) { // 遍历物品
    for(int j = bagWeight; j >= weight[i]; j--) { // 遍历背包容量
        dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);
    }
}
```

It should be noted that j iterate from high to low. If we iterate j from low to high, then every dp[j] would use the already updated value of dp[j - weight[i]] which means adding the same item multiple times. 

- LC 1049. Last Stone Weight II

  You are given an array of integers stones where stones[i] is the weight of the ith stone.
  
  We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:
  
  If x == y, both stones are destroyed, and
  If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
  At the end of the game, there is at most one stone left.
  
  Return the smallest possible weight of the left stone. If there are no stones left, return 0.

  ```
  class Solution:
      def lastStoneWeightII(self, stones):
          total_sum = sum(stones)
          target = total_sum // 2
          dp = [0] * (target + 1)
          for stone in stones:
              for j in range(target, stone - 1, -1):
                  dp[j] = max(dp[j], dp[j - stone] + stone)
          return total_sum - 2* dp[-1]
  ```

- LC 494. Target Sum

  You are given an integer array nums and an integer target.

  You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
  
  For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
  Return the number of different expressions that you can build, which evaluates to target.

  ```
  class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)  # 计算nums的总和
        if abs(target) > total_sum:
            return 0  # 此时没有方案
        if (target + total_sum) % 2 == 1:
            return 0  # 此时没有方案
        target_sum = (target + total_sum) // 2  # 目标和
        dp = [0] * (target_sum + 1)  # 创建动态规划数组，初始化为0
        dp[0] = 1  # 当目标和为0时，只有一种方案，即什么都不选
        for num in nums:
            for j in range(target_sum, num - 1, -1):
                dp[j] += dp[j - num]  # 状态转移方程，累加不同选择方式的数量
        return dp[target_sum]  # 返回达到目标和的方案数
  ```
#### Unbounded knapsack
Different from 0-1 knapsack, the unbounded knapsack problem has unlimited number of each element. If we remeber in 0-1 knapsack it is necessary to iterate bag from high to low to avoid adding same item multiple times. However, here we have unlimited number of items, thus the unbounded knapsack code would be like:

```
// 先遍历物品，再遍历背包
for(int i = 0; i < weight.size(); i++) { // 遍历物品
    for(int j = weight[i]; j <= bagWeight ; j++) { // 遍历背包容量
        dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);

    }
}
```

- LC 322. Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

```
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
```


### Stock selling

### Substring


### Other problems



