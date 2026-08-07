n = int(input("Enter number of elements: "))

arr = []
unique = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

for i in arr:
    if i not in unique:
        unique.append(i)

print("Unique Elements:", unique)
