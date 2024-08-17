n=int(input())
card=list(map(int,input().split()))
m=int(input())
num=list(map(int,input().split()))

card_count=[0]*20000001
for i in card:
    card_count[i+10000000]+=1

ans=[]
for i in num:
    ans.append(card_count[i+10000000])

print(*ans)