n=int(input())
if n==1:
    print('0')
    

    
else:
    row=0
    baseDistance=0
    rowsum=1
    rowsumlst=[1]
    for i in range(1,n-n//10000):
        rowsum+=i*6
        rowsumlst+=[rowsum]
    


    for x in range(0,len(rowsumlst)-1):
        if rowsumlst[x]<n<=rowsumlst[x+1]:
            row=x+1


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
    if row>4:
        print(distance-3)
    else:
        print(distance)