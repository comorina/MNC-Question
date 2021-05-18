# Maximum and minimum of an array using minimum number of comparisons

import sys
from datetime import datetime
init=datetime.now()


sys.stdout = open('s:/Check/CP1/output.txt','w')
sys.stdin = open('s:/Check/CP1/input.txt','r')


arr = [2 ,2, 45,74,33]
max = arr[0]
for i in range(1,len(arr)):
    if arr[i]>=max:
        max=arr[i]
print(max)


final=datetime.now()
print('Execution Time : ',format(final-init))