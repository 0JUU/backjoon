from collections import deque   # deque는 양쪽 끝에서의 빠른 삽입과 삭제를 지원하는 큐 자료구조
import sys
input = sys.stdin.readline  #명령어를 한 줄씩 처리.

N = int(input().strip())
O = deque()

for _ in range(N):
    M = input().strip().split()
    if M[0] == "push":
        O.append(M[1])
    elif M[0] == "pop":
        if len(O) > 0:
            print(O.popleft())
        else:
            print(-1)
    elif M[0] == "size":
        print(len(O))
    elif M[0] == "empty":
        print(1 if len(O) == 0 else 0)
    elif M[0] == "front":
        print(-1 if len(O) == 0 else O[0])
    elif M[0] == "back":
        print(-1 if len(O) == 0 else O[-1])


# N=int(input())
# O=[]
# for _ in range(N):
#     M=list(map(str,input().split()))
#     if M[0]=="push":
#         O.append(M[1])
#     elif M[0]=="pop":
#         if len(O)>0:
#             print(O[0])
#             O.pop(0)   # O.pop(0) 연산은 리스트의 나머지 원소들을 이동시키므로 O(N) 시간 복잡도를 가짐
#         else:
#             print(-1)
#     elif M[0]=="size":
#         print(len(O))
#     elif M[0]=="empty":
#         print(1) if len(O)==0 else print(0)
#     elif M[0]=="front":
#         print(-1) if len(O)==0 else print(O[0])
#     elif M[0]=="back":
#         print(-1) if len(O)==0 else print(O[-1])