####Example programme(1):-
##i=0
##while(i<10):
##    print(i)
##    i+=1
##
####Printing multiplication table(2):-
##num=int(input('Enter a number'))
##i=1
##
##while(i<=10):
##    print(num,'x',i,'=',i*num)
##    i+=1
##    
####separating units place(3):-
##num=int(input('Enter number'))
##while(num>0):
##  a=num%10
##  print(a)
##  num=num//10
##  
####while loop break(4):-
##i=0
##while(0,5):
##    if(i==4):
##        break
##    print(i)
##    i+=1
##
##while loop continue(5):-
##i=0
##while(0,7):
##    i+=1
##    if(i==4):
##        continue
##    print(i)
##    
####sum of digits(6):-
##num=int(input('Enter number'))
##temp=0
##while(num!=0):
##    last=num%10
##    num=num//10
##    temp=temp+last
##print('Sum of digits is',temp)
##    
####Armstrong number(7):-
##n=int(input('Enter a number'))
##a=0
##sum=0
##temp=n
##while(n>0):
##   last=n%10
##   sum=last**3
##   a=a+sum
##   n=n//10
##print(a)
##if(temp==a):
##  print('It is a Armstrong number')
##else:
##  print('It is not an Armstrong number')
##
####Prime number(8):-
##num=int(input('Enter a number'))
##a=0
##while(num>0):
## 
##
##
##
##
##
##
##
##
##
##
##
####Reverse numbers(9):-
##num=int(input('Enter a number'))
##num2=0
##while(num!=0):
##   variable=num%10
##   num2=num2*10+variable
##   num=num//10
##
##print('The reversed number is',num2)
##
##Finding power number(16):-
num=int(input('Enter a number'))
rootnum=int(input('Enter a root number'))
last=1
ans=0
while(ans<num):
   ans=rootnum**1

   last+=1
print('Square number',num,'=',last-1)

##
####with break(17):-
##temp=0
##while('True'):
##   a=int(input('Enter a number'))
##   if(a==0):
##      break
##   else:
##      temp=temp+a
##print('The sum of given number is',temp)
##
####Fibonacci sequence(18):-
##num=int(input('Enter the no.of.terms'))
##x=0
##y=1
##l=0
##print('Fibonacci sequence')
##while(l<num):
##   print(x)
##   z=x+y
##   x=y
##   y=z
##   l+=1
##
####Finding average(19):-
##n=int(input('Enter a number'))
##last=n
##a=0
##while(n>0):
##   m=int(input('Enter your subject mark'))
##   a=m+a
##   b=a//last
##   n=n-1
##print('The average is',b)

##(20):-
a=int(input('Enter a number'))
b=int(input('Enter a number'))
count=0
while(a!=0):
   x=a**count
   count+=1
   if(x==b):
      print('The number of time the code repeated is',count-1)
