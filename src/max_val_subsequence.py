# max_val_subsequence.py


def max_val(s1, s2, val_of_letter) -> (int, str):
    n = len(s1)
    m = len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # fill dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + val_of_letter[s1[i - 1]])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # post-processing: reconstruct one optimal subsequence
    i = n
    j = m
    chars = []

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1] and dp[i][j] == dp[i - 1][j - 1] + val_of_letter[s1[i - 1]]:
            chars.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            j -= 1

    chars.reverse()
    return dp[n][m], "".join(chars)