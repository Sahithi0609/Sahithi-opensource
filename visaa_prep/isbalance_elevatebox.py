n=int(input())
m=list(map(int, input().split()))
a=[]
for i in range(0,n):
    leftw=sum(m[:i])
    rightw=sum(m[i+1:])
    x=abs(leftw-rightw)
    a.append(x)
print(" ".join(map(str,a)))
