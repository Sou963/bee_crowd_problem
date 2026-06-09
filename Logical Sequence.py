n=int(input())
num=1
for i in range(n):
    a=num
    b=num*num
    c=num*num*num
    print(a,b,c)
    print(a,b+1,c+1)
    num=num+1