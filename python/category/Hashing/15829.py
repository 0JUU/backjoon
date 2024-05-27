# import string

# L=int(input()) 
# s=list(input()) 

# a=list(string.ascii_lowercase[:26])
# ad={}
# for i in a:
#     ad[i]=a.index(i)+1

# H=0
# for j in range(L):
#     H+=(ad[s[j]]*31**j)%1234567891
# print(H)
# ===============================================================
# ==> 50점 받음. 
# ==> 문제점: 모듈 사용으로 인해 숫자가 커져 오버플로우 발생할 수 있음
# ===============================================================

L=int(input()) 
s=input()

r=31
M=1234567891

H=0
for i in range(L):
    # 중간값이 커지지 않도록 mod M을 2번 연산
    H=(H+(ord(s[i])-ord('a')+1)*pow(r,i,M))%M
    # cf. pow(r,i,M): (r**i)%M
print(H)