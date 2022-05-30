#program to print prime number using function
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
        else:
            pass
    if count==2:
        print("prime number")
    else:
        print("non prime number")
n=int(input())
prime(n)