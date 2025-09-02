word = input("Enter the word: ")

word_low = word.lower()

if word_low == word_low[::-1]:
    print(word_low[::-1])
    print("True")
else:
    print("False")
    print(word_low + " is not a palindrome.")