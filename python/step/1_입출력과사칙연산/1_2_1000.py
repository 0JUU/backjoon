########################################################################
# 문제명: A+B
########################################################################
# 시간 제한 | 메모리 제한
# 2초      |  128MB
########################################################################
# 문제: 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
########################################################################
# 입력: 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력: 첫째 줄에 A+B를 출력한다.
########################################################################
# 예제 입력1: 1 2
# 예제 출력1: 3
########################################################################
# 알고리즘 분류: 수학, 구현, 사칙연산
########################################################################
# 구현코드:
N=map(int, input().split())
S=0
for i in N:
    S+=i
print(S)
########################################################################