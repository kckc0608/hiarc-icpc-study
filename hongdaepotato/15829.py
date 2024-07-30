#15829




l=int(input())
x=input()
lst=[]
for a in x:
    if a=='a':
        lst+=[1]
    if a=='b':
        lst+=[2]
    if a=='c':
        lst+=[3]
    if a=='d':
        lst+=[4]
    if a=='e':
        lst+=[5]
    if a=='f':
        lst+=[6]
    if a=='g':
        lst+=[7]
    if a=='h':
        lst+=[8]
    if a=='i':
        lst+=[9]
    if a=='j':
        lst+=[10]
    if a=='k':
        lst+=[11]
    if a=='l':
        lst+=[12]
    if a=='m':
        lst+=[13]
    if a=='n':
        lst+=[14]
    if a=='o':
        lst+=[15]
    if a=='p':
        lst+=[16]
    if a=='q':
        lst+=[17]
    if a=='r':
        lst+=[18]
    if a=='s':
        lst+=[19]
    if a=='t':
        lst+=[20]
    if a=='u':
        lst+=[21]
    if a=='v':
        lst+=[22]
    if a=='w':
        lst+=[23]
    if a=='x':
        lst+=[24]
    if a=='y':
        lst+=[25]
    if a=='z':
        lst+=[26]
 

    
sum=0
for letter in range(0,l):
    sum+=lst[letter]*31**letter
    
print(sum%1234567891)
    
