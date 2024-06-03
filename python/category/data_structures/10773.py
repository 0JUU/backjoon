# A=[]
# for _ in range(int(input())):
#     I=int(input())
#     if I>0:
#         A.append(I)
#     else:
#         A.pop()
# a=0
# for i in A:
#     a+=i
# print(a)

import sys

A=[]
for _ in range(int(sys.stdin.readline())):
    I=int(sys.stdin.readline())
    if I>0:
        A.append(I)
    else:
        A.pop()
        
print(sum(A))