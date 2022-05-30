#program to print the square of number from list
l=list(map(int,input().split()))
a=[x**2 for i in range len(l)]
print(a)