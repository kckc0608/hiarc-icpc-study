#시간 초과 문제
#lst +=는 요소 더할때마다 새 리스트 생ㅅㅇ하니까 더ㅃ른>> append로 변경
#median ㄱ ㅜ할때 sort 안함
#아직도 시간초과 
#lst.count() 쓰고 list 생성하는 대신 counter 도입하여 더 빠르게 

from collections import Counter

n=int(input())
lst=[]
for i in range(n):
    x=int(input())
    lst.append(x)

add=0
for num in lst:
    add+=num
avg=add/len(lst)
lst.sort()
median=lst[(i//2)]
count=Counter(lst)
maxc=max(count.values())
modes=[k for k, v in count.items() if v==maxc]

r4nge=max(lst)-min(lst)
    
print(round(avg))
print(round(median))
if len(modes)>=2:
    print(round(modes[1]))
elif len(modes)==1:
    print(round(modes[0]))

print(round(r4nge))