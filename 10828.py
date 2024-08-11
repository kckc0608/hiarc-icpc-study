#문제: '-1'이 중복되어 출력. 이유: pop을 실행한 다음에 []인지 판단하는 순서로 해버려서  중복으로 들어감 



n=int(input())
lst=[]
prt=[]
for i in range(n):
    x=input()
    y=list((x.split()))
    if 'push' in y:
        lst.append(y[1])
        
    elif 'pop' in y:
        if lst==[]:
            
            prt+=[-1]
        if lst!=[]:
            prt+=[lst.pop()]
            
      
  
    elif 'size' in y:
        prt+=[(len(lst))]
  
    elif 'empty' in y:
        if lst==[]:
            prt+=[1]
        if lst!=[]:
            prt+=[0]
   
    elif 'top' in y:
        if lst!=[]:
            prt+=[lst[-1]]
        if lst==[]:
            prt+=[-1]

for item in prt:
    print(item)