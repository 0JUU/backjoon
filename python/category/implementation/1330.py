#######################################################################
# 문제명: 두 수 비교하기                
#######################################################################
# 시간 제한 | 메모리 제한
# 1초      |  512MB
#######################################################################
# 문제: 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
#######################################################################
# 입력: 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.
# 출력: 첫째 줄에 다음 세 가지 중 하나를 출력한다.
#       - A가 B보다 큰 경우에는 '>'를 출력한다.
#       - A가 B보다 작은 경우에는 '<'를 출력한다.
#       - A와 B가 같은 경우에는 '=='를 출력한다.
#######################################################################
# 제한: -10,000 ≤ A, B ≤ 10,000
#######################################################################
# 예제 입력1: 1 2
# 예제 출력1: <
#---------------------
# 예제 입력2: 10 2
# 예제 출력2: >
#---------------------
# 예제 입력3: 5 5
# 예제 출력3: ==
#######################################################################
# 알고리즘 분류: 구현
#######################################################################
# 구현코드:
x,y=map(int, input().split())
if(x>y):
    print(">")
elif(x<y):
    print("<")
else:
    print("==")
#######################################################################