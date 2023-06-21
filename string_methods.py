####Umbrella(1):-
##a='Umbrella'
##result=a.find('e')
##if(result!=-1):
##    print('e is present in the string')
##else:
##    print('e is not present in the string')
##
##
####orange juice(2):-
##b='Orange Juice'
##result=b.find('Orange')
##if(result!=-1):
##    print('Orange is present in the string')
##else:
##    print('Orange is not present in the string')
##
##capitalize(3):-
txt='hello'
x=txt.capitalize()
print(x)

##casefold(4):-
txt='Hello'
x=txt.casefold()
print(x)

##center(5):-
txt='Banana'
x=txt.center(20)
print(x)

##count(6):-
txt='I love bananas,banana is my favorite fruit'
x=txt.count('banana')
print(x)

##encode(7):-
txt='My name is Kanishka'
x=txt.encode()
print(x)

##endswith(8):-
txt='Hello,Welcome to my world.'
x=txt.endswith('.')
print(x)

##expandtabs(9):-
txt='H\te\tl\tl\to'
x=txt.expandtabs(2)
print(x)
