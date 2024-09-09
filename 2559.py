#2559
#https://stackoverflow.com/questions/40336367/python-prefix-sum-algorithm
#다른 건 알겠는데, 처음에 0으로만 된 리스트를 만드는 이유가...?
n,neighbor=map(int,input().split())
lst=[]

x=list(map(int,input().split()))
pSum=[0]*(n+1)
for m in range(1,n+1):
    pSum[m]=pSum[m-1]+x[m-1]


for i in range(0,n-neighbor+1):
    lst.append(pSum[i+neighbor]-pSum[i])
    

print(max(lst))