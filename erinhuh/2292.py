n=int(input())

x=1
k=1
while True:
    if n<=x:
        print(k)
        break
    else:
        x+=k*6
        k+=1