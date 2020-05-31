class Solution:
    def fib_recursion(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        return (self.fib_recursion(n-1) + self.fib_recursion(n-2)) % 1000000007


    def fib_memo(self, n: int) -> int:
        d = dict()
        d[0] = 0
        d[1] = 1
        for i in range(2, n+1):
            d[i] = d[i-2] + d[i-1]
        return d[n] % 1000000007

    def fib_dp(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n] % 1000000007

    def fib_dp_opt(self, n: int) -> int:
        a = 0
        b = 1
        while n:
            tmp = a + b
            a = b
            b = tmp
            n -= 1
        return a % 1000000007
        