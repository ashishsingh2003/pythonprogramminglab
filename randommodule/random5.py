#program to print multiple random integer number from a sequence
import random 
l=list(map(int,input().split()))
c=random.sample(l,k=int(input()))
print(c)