a,b,v=map(int,input().split())

v_=v-a
if v_%(a-b)==0:
    print(v_//(a-b)+1)
else:
    print(v_//(a-b)+2)