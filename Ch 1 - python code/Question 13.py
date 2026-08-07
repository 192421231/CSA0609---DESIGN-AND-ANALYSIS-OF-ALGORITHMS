def climbStairs(n):
    if n <= 2:
        return n

    a = 1
    b = 2

    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c

    return b

n = int(input("Enter the number of steps: "))

print("Number of ways:", climbStairs(n))
