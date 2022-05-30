#program to find the sum of all elements present in list
l=list(map(int,input().split()))
sum=0
for i in l:
    sum=sum+i
print(sum)