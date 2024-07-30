n=int(input())
lst=list(input())

r=31
M=1234567891

keys=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
abc=dict(zip(keys,values))

sum=0
x=0
for i in lst:
    i_=abc[i]
    sum+=i_*(r**x)
    x+=1

print(sum%M)