timeteam={}
time=[]
for i in range(8):
    a,b=input().split()
    lst=list(str(a))
    lst.remove(lst[1])
    lst.remove(lst[3])
    n=0
    for i in range(6):
        n+=int(lst[i])*(10**(5-i))
    time.append(n)
    timeteam[n]=b

time.sort()

r=0
b=0
for i in range(len(time)):
    d={0:10,1:8,2:6,3:5,4:4,5:3,6:2,7:1}
    if timeteam[time[i]]=='R':
        r+=d[i]
    else:
        b+=d[i]

if r>b:
    print('Red')
else:
    print('Blue')