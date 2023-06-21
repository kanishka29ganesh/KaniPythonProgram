##swap(1):-
a=int(input('Enter a number'))
b=int(input('Enter a number'))
c=a
a=b
b=c
print(a,',',b)


##swap(2):-
a=int(input('Enter a number'))
b=int(input('Enter a number'))
a,b=b,a
print(a,',',b)
