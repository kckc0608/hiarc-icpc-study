n=int(input())
if n==1:
    print('1')
    

    
else:
    row=0
    baseDistance=0
    rowsum=1
    rowsumlst=[1]
    i=1
    while rowsum<n:
        rowsum+=i*6
        i+=1
        rowsumlst.append(rowsum)

    

    for x in range(0,len(rowsumlst)-1):
        if rowsumlst[x]<n<=rowsumlst[x+1]:
            row=x+1
            break


    points=[rowsumlst[row]]
    val=rowsumlst[row]
    while val>rowsumlst[row-1]:
    
        val=val-row
        points+=[val]

    
    baseDistancelst=[]
    for item in points:
        baseDistancelst+=[abs(item-n)]
    baseDistance=min(baseDistancelst)
    
    

    distance=baseDistance+row+1
   
    print(distance-baseDistance)
  
    
