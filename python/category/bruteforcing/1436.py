N=int(input())

def fs(N):
    cnt=0
    num=666
    while True:
        if '666' in str(num):
            cnt+=1
            if cnt==N:
                return num
        num+=1

R=fs(N)
print(R)