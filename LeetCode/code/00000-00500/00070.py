class Solution:
    def climbStairs(self, n: int) -> int:
        """
        爬到第n楼的方法，为爬到第n-1楼和n-2楼的方法之和
        因为爬到n-1楼后，再爬1楼就能到达n楼
        爬到n-2楼同理
        因此只需初始化爬到1楼和爬到2楼分别有多少种方法，便可以推导出爬到n楼的方法
        """
        first = 1  # 爬到1楼只有1种方法
        second = 2  # 爬到2楼有两种方法
        res = 0  # 初始化爬到n楼的方法
        for i in range(2, n):  # 从3楼开始算
            res = first + second

            first = second  # 推导下一层
            second = res

        return max(n, res)  # 返回n和res中较大的那个

    def dp_method(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0 for _ in range(n + 1)]  # dp[i]表示爬到第i阶的方法数
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]  # or return dp[n]
