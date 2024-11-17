n=int(input())
for i in range(0,n):
    x,y=map(int, input().split())
    z=x//10
    result=z*y
    print(result)
