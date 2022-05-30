#program to print armstrong number using function
def armstrong(n):
    d=0
    c=n
    sum=0
    temp=n
    while(n>0):
        n=n//10
        d+=1
    while(c>0):
        r=c%10
        c=c//10
        sum=sum+r**d
    if temp==sum:
        print("armstrong number")
    else:
        print("not armstrong number")
b=int(input())
armstrong(b)
