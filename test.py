dp = {
    0: 0,
    1: 1
}

def get_fibo(n, dp):
    if n in dp:
        return dp[n]
    else:
        dp[n] = get_fibo(n-1, dp) + get_fibo(n-2, dp)
        return dp[n]


def solution(n):
    answer = get_fibo(n, dp)%1234567
    return answer

solution(100000)