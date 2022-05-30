#program to print a random integer number from a sequence
import random 
l=list(map(int,input().split()))
c=random.choice(l)
print(c)