#program to print perfect using function
def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
        else:
            pass
    if n==sum:
        print("perfect number")
    else:
        print("not perfect number")
b=int(input())
perfect(b)