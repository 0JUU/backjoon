##################################################################
# 문제명: 별 찍기 - 7
##################################################################
# 시간 제한 | 메모리 제한
# 1초      |  128MB
##################################################################
# 문제: 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
##################################################################
# 입력: 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 출력: 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
##################################################################
# 예제 입력1: 5
# 예제 출력1:     *
#              ***
#             *****
#            *******
#           *********
#            *******
#             *****
#              ***
#               *
##################################################################
# 알고리즘 분류: 구현
##################################################################
# 구현코드:
N=int(input())
a=2*N//2
b=2*N-1
for i in range(a):
    print(" "*(N-(i+1))+"*"*(2*i+1))
for j in range(b-a):
    print(" "*(j+1)+"*"*(2*(i-j)-1))
##################################################################
