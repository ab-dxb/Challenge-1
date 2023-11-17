# Palindrome or not

string = input("Enter the string: ")
string = string.lower()
length_string = len(string)
is_palindrome = True

for letter in range(length_string // 2):
    if string[letter] != string[length_string - letter - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print(string, "DAMN IT is a palindrome you SMART AS HELL DAWG")
else:
    print(string, "YOU ILLITERATE DAWG IT IS not A PALINDROME")
