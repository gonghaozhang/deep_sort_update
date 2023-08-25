def levenshtein_with_operations(A, B):
    m, n = len(A), len(B)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    actions = [['' for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
                actions[i][j] = 'I'
            elif j == 0:
                dp[i][j] = i
                actions[i][j] = 'D'
            elif A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]
                actions[i][j] = 'N'  # No change required
            else:
                insert = dp[i][j-1] + 1
                delete = dp[i-1][j] + 1
                replace = dp[i-1][j-1] + 1

                dp[i][j] = min(insert, delete, replace)
                
                if dp[i][j] == insert:
                    actions[i][j] = 'I'
                elif dp[i][j] == delete:
                    actions[i][j] = 'D'
                else:
                    actions[i][j] = 'M'

    i, j = m, n
    operations = []

    while i > 0 or j > 0:
        if actions[i][j] == 'M':
            operations.append(f"Modify {A[i-1]} to {B[j-1]} at position {i-1}")
            i, j = i-1, j-1
        elif actions[i][j] == 'D':
            operations.append(f"Delete {A[i-1]} at position {i-1}")
            i -= 1
        elif actions[i][j] == 'I':
            operations.append(f"Insert {B[j-1]} at position {j-1}")
            j -= 1
        else:  # 'N' for no change
            i, j = i-1, j-1

    return dp[m][n], operations[::-1]

A = "dae"
B = "days"
distance, ops = levenshtein_with_operations(A, B)
print(f"Distance: {distance}")
for op in ops:
    print(op)

