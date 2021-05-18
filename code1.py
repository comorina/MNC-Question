#Reverse Array--------->

import sys
from datetime import datetime
init=datetime.now()


sys.stdout = open('s:/Check/CP1/output.txt','w')
sys.stdin = open('s:/Check/CP1/input.txt','r')

N = int(input())
arr=[]

for i in range(N):
    l = int(input())
    arr.append(l)

arr_rev = []
for i in range(len(arr)-1,-1,-1):
    arr_rev.append(arr[i])
print(arr_rev)


final=datetime.now()
print('Execution Time : ',format(final-init))