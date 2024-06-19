mystring = str(input())
if mystring == mystring[::-1]:
    print(mystring, "is a palindrome")
else:
    print(mystring, "is not a palindrome")