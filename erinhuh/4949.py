lst=[]
while True:
    x=list(input())
    if x==['.']:
        break
    else:
        ans=[]
        while True:
            if len(x)==0:
                break
            a=x.pop()
            if a==']' or a==')':
                ans.append(a)
            elif a=='[':
                if len(ans)==0:
                    ans.append(a)
                    break
                else:
                    b=ans.pop()
                    if b==']':
                        continue
                    else:
                        ans.append(b)
                        break
            elif a=='(':
                if len(ans)==0:
                    ans.append(a)
                    break
                else:
                    b=ans.pop()
                    if b==')':
                        continue
                    else:
                        ans.append(b)
                        break
            else:
                continue
        
        if len(ans)==0:
            lst.append('yes')
        else:
            lst.append('no')

for i in lst:
    print(i)