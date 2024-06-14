###### 학점계산
G=input()
grade=['A','B','C','D']

if G=='F':
    result=0.0
else:
    value=grade.index(G[0])
    if G[1]=='+':
        result=4.3-value
    elif G[1]=='0':
        result=4.0-value
    elif G[1]=='-':
        result=3.7-value

print(round(result,2))
####################################
# G = input()
# grade = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}

# if G == 'F':
#     result = 0.0
# else:
#     base = grade[G[0]]
#     modifier = {'+': 0.3, '0': 0.0, '-': -0.3}
#     result = base + modifier[G[1]]

# print(result)