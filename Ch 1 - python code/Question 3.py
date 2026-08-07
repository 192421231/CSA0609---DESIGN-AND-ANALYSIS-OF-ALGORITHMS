def sum_of_squares(nums):
    total = 0
    n = len(nums)

    for i in range(n):
        s = set()

        for j in range(i, n):
            s.add(nums[j])
            distinct = len(s)
            total = total + distinct * distinct

    return total

n = int(input("Enter the number of elements: "))

nums = []

print("Enter the elements:")
for i in range(n):
    nums.append(int(input()))

answer = sum_of_squares(nums)

print("Output:", answer)
