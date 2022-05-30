#program to remove the repeating element from the list
l=list(map(int,input().split()))
a=[]
for i in l:
    if i in a:
        pass
    else:
        a.append(i)
print(a)