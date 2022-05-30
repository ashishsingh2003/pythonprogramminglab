#program to print the even no. from list
l=list(map(int,input().split()))
a=[]
for i in l:
    if i%2==0:
        a.append(i)
    else:
        pass
print(a)