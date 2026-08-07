def findMax(arr):
    maximum = arr[0]

    for i in arr:
        if i > maximum:
            maximum = i

    return maximum

n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

print("Output:", findMax(arr))
