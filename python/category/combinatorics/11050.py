########################################################################################
# 문제명: 이항 계수 1
########################################################################################
# 시간 제한 | 메모리 제한
# 1초      |  256
########################################################################################
# 문제: 자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 
# \(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.
########################################################################################
# 입력: 첫째 줄에 \(N\)과 \(K\)가 주어진다. (1 ≤ \(N\) ≤ 10, 0 ≤ \(K\) ≤ \(N\))
# 출력: \(\binom{N}{K}\)를 출력한다.
########################################################################################
# 예제 입력1: 5 2
# 예제 출력1: 10
########################################################################################
# 알고리즘 분류: 수학, 구현, 조합론
########################################################################################
# 구현코드:
N,K=map(int,input().split())
f=1
e=1
h=1
for i in range(1,N+1):
    f*=i
for j in range(1,K+1):
    e*=j
for k in range(1,N-K+1):
    h*=k
print(f//(h*e))
########################################################################################