####Syntax of for loop(1):-
##for a in range(1,10):
##    print(a)
##
##
####Syntax of for loop(2):-
##for a in range(1,20,2):
##    print(a)
##
##
####syntax of for loop(3):-
##for a in range(2,21,2):
##    print(a)
##
##
####syntax of for loop(4):-
##for a in range(0,101):
##    print(a)
##
##
####Get value from user and find range(5):-
##value=int(input('Enter a stop value'))
##
##for i in range(1,value):
##    print(i)
##
##
####print multiples of number given(6):-
##num=int(input('Enter a number'))
##
##for i in range(num,num*11,num):
##    print(i)
##
##
####print multiples of number given in table form(7):-
##num=int(input('Enter a number'))
##
##for i in range(1,11):
##    print(i,'*',num,'=',i*num)
##     
####Printing 1 to 50 and incating multiples of 3&5(9):-
##
##for i in range(1,51):
##    
##    if(i%3==0 and i%5==0):
##        print(,'=','FizzBuzz')
##    elif(i%3==0):
##        print('=','Fizz')
##    elif(i%5==0):
##        print('=','Buzz')
##
##    print(i)
##    
####Getting value from user and finding it's factorial(10):-
##num=int(input('Enter a value'))
##temp=1
##
##for i in range(1,num+1):
##    temp=temp*i
##print('Factorial of',num,'is',temp)
##
##
####Sum of numbers(11):-
##num=int(input('Enter a value'))
##temp=0
##
##for i in range(1,num+1):
##    temp=temp+i
##print('Sum of number of',num,'is',temp)
##
##printing even numbers(12):-
##num=int(input('Enter an even number'))
##temp=0
##for i in range(2,2*(num+1),2):
##    temp=temp+i
##print('Sum of even numbers',temp)
##
####Printing prime numbers(13):-
##for i in range(2,100):
##    if(i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%7!=0 and i%9!=0 or i==2 or i==3 or i==5):
##        print(i)
####for loop break(14):-
##for i in range(0,5):
##    if(i==4):
##        break
##    print(i)
##
####for loop continue(15):-
##for i in range(0,7):
##    if(i==4):
##        continue
##    print(i)
##
####Printing 1-20 without multipes of 2 and 3(16):-
##for i in range(1,21):
##    if(i%2==0 and i%3==0):
##        pass
##    else:
##        print(i)
##
####maximum(17):-
##n=input('Enter input')
##for i in range(0,len(n)):
##    print(n[i])
##
##print('\n')
##
##for i in n:
##    print(i)
##
####(18):-
##n=input('Enter value')
##for i in range(0,len(n)):
##    print(n[i])
##
####(19):-
##for i in range(0,6):
##    if(i==4):
##        break
##    print(i)
##print('\n')
## for j in range(1,10):
##     if(j==7):
##         continue
##    print(j)
##else:
##    print('Completed')

##(20):-
n=input('Enter number')

print('The digits are:')
for i in n:
     print(i)
