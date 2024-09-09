#11659
#2559번 활용
#합이 잘못 구해지는 오류
#pSum[b+1]- pSum[a+1] x, pSum[b[-pSum[a] o. 맨 앞 숫자 인덱스는 0 인데 input 은 1
n,m=map(int,input().split())


x=list(map(int,input().split()))
pSum=[0]*(n+1)
for y in range(1,n+1):
    pSum[y]=pSum[y-1]+x[y-1]


for i in range(m):
    a,b=map(int,input().split())
    print(pSum[b]-pSum[a-1])
    

