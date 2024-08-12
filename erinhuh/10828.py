n=int(input())

stack=[]
ans=[]
for i in range(n):
    lst=list(input().split())
    if lst[0]=='push':
        stack.append(lst[1])
    elif lst[0]=='top':
        if len(stack)==0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
    elif lst[0]=='size':
        ans.append(len(stack))
    elif lst[0]=='pop':
        if len(stack)==0:
            ans.append(-1)
        else:
            x=stack.pop()
            ans.append(x)
    elif lst[0]=='empty':
        if len(stack)==0:
            ans.append(1)
        else:
            ans.append(0)

for i in ans:
    print(i)