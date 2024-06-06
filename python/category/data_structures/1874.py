import sys

def stack_seq(n,seq):
    stack=[]
    rst=[]
    curr=1
    possible=True

    for num in seq:
        while curr <= num:
            stack.append(curr)
            rst.append('+')
            curr+=1
        if stack and stack[-1] == num:
            stack.pop()
            rst.append('-')
        else:
            possible=False
            break

    if possible:
        print('\n'.join(rst))
    else:
        print('NO')

input=sys.stdin.readline
n=int(input().strip())
seq=[int(input().strip()) for _ in range(n)]

stack_seq(n,seq)