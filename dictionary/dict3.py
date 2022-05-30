#program to reverse the order of dictionary
q={}
l=[input() for i in range(2)]
m=[input() for i in range(2)]
a=l[::-1]
b=m[::-1]
for i in range(len(a)):
        q[a[i]]=b[i]
print(q)
