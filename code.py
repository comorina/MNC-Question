import sys
from datetime import datetime

sys.stdout = open("s:\Check\CP1\output.txt","w")
sys.stdin = open("s:\Check\CP1\input.txt","r")



def g():
    x=input()
    c=0
    if(x[0]=='1'):
        c+=1
    for i in range(1,len(x)):
        if(x[i]=='1' and x[i-1]!='1'):
            c+=1
    print(c)
init=datetime.now()
for i in range(int(input())):
    g()
final=datetime.now()
print('initial time: ',init)
print('final time: ',final)
print('Execution Time :',(final-init))
