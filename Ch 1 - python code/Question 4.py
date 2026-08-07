def countPairs(nums, k):
    count = 0
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j] and (i * j) % k == 0:
                count += 1

    return count

n = int(input("Enter number of elements: "))

nums = []
print("Enter the elements:")
for i in range(n):
    nums.append(int(input()))

k = int(input("Enter k: "))

print("Output:", countPairs(nums, k))
