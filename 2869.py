#풀이 1- 오류발생
import math



# a,b,v=map(int,input().split())
# cycle=a-b

#progress=0
#count=0

#while v-progress>a:
    #progress+=cycle
  
    #count+=1
#print(count+1)
    
##########################################
#풀이 2
a,b,v=map(int,input().split())
cycle=a-b
days=math.ceil(((v-a)/cycle))
if a>=v:
    print(1)
else:
    print(days+1)
    