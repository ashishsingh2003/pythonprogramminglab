#program to left rotate the list
l=list(map(int,input().split()))
n=int(input("enter number to rotate\n"))
for i in range(len(l)-n):
    l[i],l[i+n]=l[i+n],l[i]
print(l)