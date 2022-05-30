#program to print multiple random integer number from a sequence
import random 
l=list(map(int,input().split()))
k=int(input())
c=random.choice(l,k)
print(c)