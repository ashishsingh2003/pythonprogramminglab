#program to right rotate the list
l=list(map(int,input().split()))
n=int(input("enter number to rotate\n"))
for i in range(len(l)):
    l[i],l[len(l)-n]=l[len(l)-n],l[i]
print(l)