T=int(input())
for _ in range(T):
    C=int(input())
    Q=C//25
    QM=C%25
    D=QM//10
    DM=QM%10
    N=DM//5
    P=DM%5
    print(Q,D,N,P)