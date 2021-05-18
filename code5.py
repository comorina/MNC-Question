import sys
from datetime import datetime

init=datetime.now()

sys.stdout = open('s:/Check/CP1/output.txt','w')
sys.stdin = open('s:/Check/CP1/input.txt','r')

n,m=map(int,input().split())
arr=[]

for i in range(n):
    l=[]
    for j in range(m):
        l.append(int(input()))
    arr.append(l)


final=datetime.now()
print('Execution Time : ',format(final-init))