#16139
#자꾸 원래 답보다 1씩 작은 수나 1씩 큰 수가  출력되는 문제가 발생(해결)
#pSum 식에서 [] 안의 수를 1씩 뺌
#반례: 같은 수 (4 4) 쓸때 그걸 세지 못함 (해결)
#조건문으로 경우를 나눔
#인덱스 0-based, 1-based 섞지말고 0 based로만 변경하기(완료)
#조건 세부화(완료)


x=input()
n=int(input())
pSum=[0]*(len(x))
d,e,f=(input().split())
e=int(e)
f=int(f)
for y in range(0,len(x)):
    if y==0:
        if x[y]==d:
            pSum[y]=1
        else:
            pSum[y]=0
    else:
        if x[y]==d:
            pSum[y]=pSum[y-1]+1
        else:
            pSum[y]=pSum[y-1]

if e==f : 
    if  x[e]==d:
        print(1)  
    else:
        print(0)
else:
    if e>0:
        print(pSum[f]-pSum[e-1])
    elif e==0:
        print(pSum[f])
    
for i in range(n-1):
    a,b,c=(input().split())
    b=int(b)
    c=int(c)
    if  b==c:
        if x[b]==a:
            print(1)
        else:
            print(0)
    else:
        if b>0:
            print(pSum[c]-pSum[b-1])
        else:
            print(pSum[c])

    
    

    