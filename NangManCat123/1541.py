temp=input().split("-")
arr=[]
for i in temp:
    sum=0
    num=i.split("+")
    for j in num:
        sum+=int(j)
    arr.append(sum)
res=arr[0]
for i in range(1,len(arr)):
    res-=arr[i]
print(res)