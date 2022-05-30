#program to autocomplete the word
l=list(map(str,input().split()))
n=input()
x=[]
for i in l:
    if n in i:
        x.append(i)
print(x)
