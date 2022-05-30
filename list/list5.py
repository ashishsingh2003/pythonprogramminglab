#program to find the second largest element in list
l=list(map(int,input().split()))
l.sort()
print(l[-2])