n = int(input("Enter number of elements: "))

arr = []

if n == 0:
    print("List is empty")
else:
    print("Enter the elements:")
    for i in range(n):
        arr.append(int(input()))

    arr.sort()

    print("Sorted List:", arr)
    print("Maximum Element:", arr[-1])
