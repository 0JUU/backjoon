N=int(input())
M=[]
for i in range(N):
    a,n=input().split()
    a=int(a)
    M.append((a,n,i))
# 나이(a)와 인덱스(i) 기준으로 정렬
M.sort(key=lambda m:(m[0],m[2]))
for m in M:
    print(m[0],m[1])