import sys
from datetime import datetime
init=datetime.now()


sys.stdout = open('s:/Check/CP1/output.txt','w')
sys.stdin = open('s:/Check/CP1/input.txt','r')



N,K = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
print(arr[K])
     

final=datetime.now()
print('Execution Time : ',format(final-init))