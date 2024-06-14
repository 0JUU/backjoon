##### 진법 변환
# def convert(N,B):
#     digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     result=""

#     while N>0:
#         result=digits[N%B]+result
#         N//=B

#     return result

# # def convert(N,B):
# #     if N==0:
# #         return "0"
    
# #     digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# #     result=[]

# #     while N>0:
# #         result.append(digits[N%B])
# #         N//=B

# #     result.reverse()
# #     return ''.join(result)  # join() - 문자열 연결을 효율적으로 처리

# N,B=map(int,input().split())
# print(convert(N,B))

########################################
N,B=map(int,input().split())

digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result=""

while N:
    result+=digits[N%B]
    N//=B

print(result[::-1])