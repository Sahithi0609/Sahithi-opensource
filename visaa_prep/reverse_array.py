n=int(input())
m=list(map(int, input().split()))
for i in range(0,n):
    print(m[n-i-1],end=" ")
