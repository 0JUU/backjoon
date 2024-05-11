##########################################################################
# 문제명: 별 찍기 - 2     
##########################################################################
# 시간 제한 | 메모리 제한
# 1초      |  128MB
##########################################################################
# 문제: 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
#       하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.
##########################################################################
# 입력: 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 출력: 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
##########################################################################
# 예제 입력1: 5
# 예제 출력1:     *
#               **
#              ***
#             ****
#            *****
##########################################################################
# 알고리즘 분류: 구현
##########################################################################
# 구현코드:
T=int(input())
for i in range(1,T+1):
    for j in range(T-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()
##########################################################################