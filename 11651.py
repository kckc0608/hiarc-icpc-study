#11651

#return a,b 했더니 거꾸로 정렬되길래 그냥 return b,a 로 바꿨는데 제대로 정렬되었
def keyy(x):
    a,b=map(int,x.split())
    
    return a,b

n=int(input())
lst=[]

for i in range(n):
    x=input()
    lst.append(x)
    
    
    



lst.sort(key=keyy)
for x in lst:
    print(x)

