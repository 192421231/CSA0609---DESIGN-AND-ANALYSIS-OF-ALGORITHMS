def first_palindrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""

n = int(input("Enter the number of words: "))

words = []

print("Enter the words:")
for i in range(n):
    words.append(input())

result = first_palindrome(words)

print("First Palindromic String:", result)
