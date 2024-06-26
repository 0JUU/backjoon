####################################################################
# 문제명: 진법 변환
####################################################################
# 시간 제한 | 메모리 제한
# 1초      |  128MB
####################################################################
# 문제: B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
#      10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 
#      이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
#      A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35
####################################################################
# 입력: 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)
#      B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.
# 출력: 첫째 줄에 B진법 수 N을 10진법으로 출력한다.
####################################################################
# 예제 입력1: ZZZZZ 36
# 예제 출력1: 60466175
####################################################################
# 알고리즘 분류: 수학, 구현, 문자열
####################################################################
# 구현코드:
def ctd(N,B):  # 10진법으로 변환하는 함수
    decimal=0  # decimal:10진법으로 변환된 수를 저장할 변수
    # B진법 수의 각 digit(자리수)에 대해 반복문 수행(첫번째 자리부터)
    for i,digit in enumerate(N[::-1]):
        if digit.isdigit():  # digit이 숫자인 경우
            # 10진법으로 변환한 후 합산
            decimal+=int(digit)*(B**i)
        else:  # digit이 알파벳인 경우
            # 그 digit에 해당하는 숫자로 변환한 후 합산
            # ord('A')==65 -> 10진수로 변환을 위해 55를 빼야 함(10진수 A: 10)
            decimal+=(ord(digit)-55)*(B**i)
    return decimal
N,B=input().split()
decimal=ctd(N,int(B))
print(decimal)
####################################################################
# 누군가가 제출한 코드:
# a,b=input().split()
# print(int(a,int(b)))
# 내가 작성한 코드와 동일한 결과를 가져온다.
# int(b)가 먼저 호출되어 b를 10진법으로 변환한 후 변환된 b가 a를 변환한다.
####################################################################