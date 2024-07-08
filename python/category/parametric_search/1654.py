def maxlen(len,K,N):
    L=1
    R=max(len)
    maxLen=0
    while L <= R:
        mid=(L+R)//2
        cnt=0

        

K,N=map(int,input().split())
len=[]
for i in range(K):
    len[i]=int(input())
print(maxlen(len,K,N))    
