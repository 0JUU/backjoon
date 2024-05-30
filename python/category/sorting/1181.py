N=int(input())
M=[input() for _ in range(N)]
O=sorted(set(M),key=lambda x:(len(x),x))
for i in O:
    print(i)