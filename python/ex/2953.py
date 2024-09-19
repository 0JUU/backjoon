man = [list(map(int, input().split())) for _ in range(5)]
man_score = [0] * 5
score = 0

for i in range(5):
    sum = 0
    for j in range(4):
        sum += man[i][j]
    man_score[i] = sum
    score = max(score, sum)

for i in range(5):
    if man_score[i] == score:
        print(i + 1, score)
        break