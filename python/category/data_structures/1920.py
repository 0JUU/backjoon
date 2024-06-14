###### 수 찾기
N=int(input())
arr1=set(map(int,input().split()))
M=int(input())
arr2=list(map(int,input().split()))

result=[]
for i in arr2:
    if i in arr1:
        result.append('1')
    else:
        result.append('0')
print('\n'.join(result))