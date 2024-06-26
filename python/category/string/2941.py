###################################################################################
# 문제명: 크로아티아 알파벳
###################################################################################
# 시간 제한 | 메모리 제한
# 1초      |  128MB
###################################################################################
# 문제: 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 
#      따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.
#      크로아티아 알파벳 | č  | ć  | dž  | đ  | lj | nj | š  | ž
#      변경          | c=  | c- | dz= | d- | lj | nj | s= | z=
#      예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 
#      단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
#      dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 
#      위 목록에 없는 알파벳은 한 글자씩 센다.
###################################################################################
# 입력: 첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
#      단어는 크로아티아 알파벳으로 이루어져 있다. 
#      문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.
# 출력: 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
###################################################################################
# 예제 입력1: ljes=njak
# 예제 출력1: 6
#--------------------
# 예제 입력2: ddz=z=
# 예제 출력2: 3
###################################################################################
# 알고리즘 분류: 구현, 문자열
###################################################################################
# 구현코드:
# ##FIRST CODE##
# d=['c=','c-','dz=','d-','lj','nj','s=','z=']
# w=input()
# c=0
# for i in d:
#     if w.find(i)!=-1:
#         c+=1
#         w=w.replace(i," ")
# print(len(w.replace(" ",""))+c)
# ==> 틀린 코드. d에 해당하는 값을 w에서 공백으로 변환한 후 다시 공백을 없앤 뒤의 w 길이를 체크함.
#     그러나 이는 공백을 제외한 나머지 문자들이 그 패턴에 해당하는 경우가 있으므로 해당 코드는 잘못되었다.

# ##SECOND CODE##
d=['c=','c-','dz=','d-','lj','nj','s=','z=']
w=input()
c=0
for i in d:
    if i in w:
        c+=w.count(i)
print(len(w)-c)
# ==> 정답 코드. 공백으로 변환하지 않고 문자열의 길이만 체크하여 카운트를 더했다.
###################################################################################
