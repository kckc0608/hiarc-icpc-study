n=int(input())
lst=list(map(int,input().split()))
lst.sort()
m=int(input())
find=list(map(int,input().split()))
ans=[]
for i in find:
    low=0
    high=len(lst)-1
    while True:
        mid=int((low+high)/2)
        if lst[mid]==i:
            ans.append(1)
            break
        elif i<lst[mid]:
            high=mid-1
        elif i>lst[mid]:
            low=mid+1
        if high<low:
            ans.append(0)
            break
for i in ans:
    print(i)