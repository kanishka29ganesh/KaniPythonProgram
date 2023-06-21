##Bitwise and:-
a=int(input('Enter a number'))
b=int(input('Enter a number'))
print(a&b)

####Bitwise or:-
a= int(input('Enter a number'))
b=int(input('Enter a number'))
print(a|b)

##Bitwise complement:-
a=int(input('Enter a number'))
b=int(input('Enter a number'))
print(a^b)

##Bitwise xor:-
a=int(input('Enter a number'))
b=int(input('Enter a number'))
print(~a)
print(~b)

##Bitwise right shift:-
a=int(input('Enter a number'))
print(a>>2)

##Bitwise left shift:-
a=int(input('Enter a number'))
print(a<<2)

##Getting value from user:-
a=int(input('Enter a three digit number'))
b=int(input('Enter a three digit number'))
if(a>99 and a<=999 and b>99 and b<=999):
   print(a&b)
   print(a|b)
   print(a^b)
   print(~a)
   print(~b)
   print(a>>2)
   print(b>>2)
   print(a<<2)
   print(b<<2)
else:
    print('Invalid Input')

