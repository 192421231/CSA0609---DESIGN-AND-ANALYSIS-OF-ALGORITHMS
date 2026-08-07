def find_intersection_values(nums1, nums2):
    answer1 = 0
    answer2 = 0

    for num in nums1:
        if num in nums2:
            answer1 += 1

    for num in nums2:
        if num in nums1:
            answer2 += 1

    return [answer1, answer2]

n = int(input("Enter the size of nums1: "))
nums1 = []

print("Enter the elements of nums1:")
for i in range(n):
    nums1.append(int(input()))

m = int(input("Enter the size of nums2: "))
nums2 = []

print("Enter the elements of nums2:")
for i in range(m):
    nums2.append(int(input()))

result = find_intersection_values(nums1, nums2)

print("Output:", result)
