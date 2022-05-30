#program to sort dictionary by key
d={}
for i in range(3):
    d[input()]=input("enter value\n")
a=dict(sorted(d.items(),key=lambda x:x[0]))
print(a)
