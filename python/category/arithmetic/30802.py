N=int(input())
S,M,L,XL,XXL,XXXL=map(int,input().split())
T,P=map(int,input().split())

shirt_orders = [
    (S + T - 1) // T,
    (M + T - 1) // T,
    (L + T - 1) // T,
    (XL + T - 1) // T,
    (XXL + T - 1) // T,
    (XXXL + T - 1) // T
]
min_shirt_orders = sum(shirt_orders)
print(min_shirt_orders)

max_pen_orders = N // P
remaining_pens = N % P
print(f"{max_pen_orders} {remaining_pens}")