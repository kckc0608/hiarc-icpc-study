#28702

a=input()
b=input()
c=input()
d=0
if 'z' not in a:
    a=int(a)
    d=a+3
    if d%15 in [3,6,9,12]:
        print('Fizz')
    elif d%15 in [5,6,10]:
        print('Buzz')
    elif d%15==0:
        print('FizzBuzz')
    else:
        print(d)
    
        
elif 'z' not in b:
    b=int(b)
    d=b+2
    if d%15 in [3,6,9,12]:
        print('Fizz')
    elif d%15 in [5,10]:
        print('Buzz')
    elif d%15==0:
        print('FizzBuzz')
    else:
        print(d)
        
   
elif 'z' not in c:
    c=int(c)
    d=c+1
    if d%15 in [3,6,9,12]:
        print('Fizz')
    elif d%15 in [5,10]:
        print('Buzz')
    elif d%15==0:
        print('FizzBuzz')
    else:
        print(d)
