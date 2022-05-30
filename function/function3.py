#program to print palindrome using function
def palindrome(n):
    a=n[::-1]
    if n==a:
        print("palindrome")
    else:
        print("not palindrome")
b=input()
palindrome(b)
