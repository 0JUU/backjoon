import sys
I = sys.stdin.read
N = int(sys.stdin.readline())
c = [0] * 10001
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    c[num] += 1
for i in range(10001):
    if c[i] > 0:
        for _ in range(c[i]):
            sys.stdout.write(f"{i}\n")
