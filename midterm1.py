#MATH 4707 midterm #1 algorithms
from itertools import permutations
from math import sqrt

#problem 1, COMMITTEE

U = set(permutations('COMMITTEE'))
print(len(U))

MTE = set()
for p in list(U):
    for i in range(0,8):
        if p[i:i+1] == p[i+1:i+2]:
            MTE.add(p)
            break
print(len(U)-len(MTE))


#problem 2
n = int(input('n value: '))
[a,b]=[0,1]
for i in range(0,n):
    [a,b]=[b,2*b+a]

print(b/a)
print(b/a-(1+sqrt(2)))


#problem 4
n = int(input('n value: '))
U = ['1','2','3']
for i in range(0,n-1):
    for j,el in list(enumerate(U)):
        U.append(el+'2')
        U.append(el+'3')
        U[j]+='1'

c = 0
for el in U:
    [is1,is2,is3]=[False,False,False]
    for s in el:
        if   s == '1': is1=True
        elif s == '2': is2=True
        else: is3 = True
        if is1 and is2 and is3:
            c+=1
            break
        
print(c)
print(3**n-3*2**n+3)




