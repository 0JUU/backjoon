N=int(input())
M=1
cnt=0
for i in range(1,N+1)[::-1]:
    M*=i
for j in str(M)[::-1]:
    if j=='0':
        cnt+=1
    else:
        break
print(cnt)