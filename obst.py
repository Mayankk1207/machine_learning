def optimal_bst(p, q, n):
    e = [[0] * (n + 1) for _ in range(n + 1)]
    w = [[0] * (n + 1) for _ in range(n + 1)]
    root = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]

    for length in range(1, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            e[i][j] = float('inf')
            w[i][j] = w[i][j - 1] + p[j - 1] + q[j]
            for r in range(i, j + 1):
                cost = e[i][r - 1] + e[r + 1][j] + w[i][j] if r < j else e[i][r - 1] + w[i][j]
                if cost < e[i][j]:
                    e[i][j] = cost
                    root[i][j] = r

    return e[1][n], root

def print_root(root, i, j):
    if i <= j:
        r = root[i][j]
        print(f"Root of subtree with keys K{i} to K{j}: K{r}")
        print_root(root, i, r - 1)
        print_root(root, r + 1, j)

p = [0.20, 0.25, 0.30, 0.15]
q = [0.10, 0.15, 0.20, 0.05, 0.10]
n = len(p)

min_cost, root = optimal_bst(p, q, n)

print(f"Minimum search cost: {min_cost}")
print("Optimal BST structure:")
print_root(root, 1, n)

