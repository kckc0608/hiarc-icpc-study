lst=[]
for i in range(3):
    n=input()
    lst.append(n)

a=0
for i in range(len(lst)):
    if lst[i]=='Fizz' or lst[i]=='FizzBuzz' or lst[i]=='Buzz':
        continue
    else:
        a=int(lst[i])+(3-i)

if a%3==0:
    if a%5==0:
        print('FizzBuzz')
    else:
        print('Fizz')
elif a%5==0 and a%3!=0:
    print('Buzz')
else:
    print(a)