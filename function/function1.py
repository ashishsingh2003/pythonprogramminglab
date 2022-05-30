#program to print even number from list using function
def even(l):
    a=[]
    for i in l:
        if i%2==0:
            a.append(i)
        else:
            pass
    print(a)
b=list(map(int,input().split()))
even(b)