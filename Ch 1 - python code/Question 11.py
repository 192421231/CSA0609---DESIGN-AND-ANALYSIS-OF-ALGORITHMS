def findPaths(m, n, N, i, j):
    memo = {}

    def dfs(x, y, steps):
        if x < 0 or x >= m or y < 0 or y >= n:
            return 1
        if steps == 0:
            return 0

        if (x, y, steps) in memo:
            return memo[(x, y, steps)]

        ways = (dfs(x + 1, y, steps - 1) +
                dfs(x - 1, y, steps - 1) +
                dfs(x, y + 1, steps - 1) +
                dfs(x, y - 1, steps - 1))

        memo[(x, y, steps)] = ways
        return ways

    return dfs(i, j, N)

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
N = int(input("Enter number of steps: "))
i = int(input("Enter starting row: "))
j = int(input("Enter starting column: "))

print("Output:", findPaths(m, n, N, i, j))
