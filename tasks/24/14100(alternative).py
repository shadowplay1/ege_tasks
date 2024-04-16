def max_subsequence_length(s):
    substrings = ["ABA", "CB", "AC", "BB", "ABC", "BCB", "BA", "AB"]
    n = len(s)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for sub in substrings:
            sub_len = len(sub)
            if i >= sub_len and s[i-sub_len:i] == sub:
                dp[i] = max(dp[i], dp[i-sub_len] + sub_len)

    return max(dp)

f=open('txt/24-14100_14100.txt').readline()
print(max_subsequence_length(f))