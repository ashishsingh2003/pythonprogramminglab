#program to print the list in descending order
l=list(map(int,input().split()))
l.sort()
print(l[::-1])