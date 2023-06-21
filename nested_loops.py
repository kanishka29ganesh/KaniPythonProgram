####Nested for loop(1):-
##for i in range(5):
##    for j in range(3):
##         print(i,',',j)
##
####Nested for loop(2):-
##for i in range(6):
##    for j in range(4):
##        for k in range(2):
##          print(i,',',j,',',k)
          
##Nested for loop in matrix form(3):-
for i in range(5):
    for j in range(5):
        print('*',end=' ')
    print()

##Nested for loop in matrix form (4):-
for i in range(5):
    for j in range(5):
        print(j+1,end=' ')
    print()

##Nested for loop in tree method(5):-
for i in range(5):
    for j in range(5):
        if(i>=j):
            print('*',end=' ')
    print()

##Nested for loop in tree method(6):-
for i in range(5):
    for j in range(5):
        if(i>=j):
          print(i+1,end=' ')
    print()

##Nested for loop in tree method(7):-
for i in range(1,6):
    for j in range(1,6):
        if(i>=j):
          print(j,end='  ')
    print()

##Nested for loop in tree method(8):-
for i in range(1,11,2):
    for j in range(1,11,2):
        if(i%2!=0 and i>=j):
          print(i,end=' ')
    print()

##Nested for loop in tree method(9):-
for i in range(2,11,2):
    for j in range(2,11,2):
        if(i>2 and i>=j):
            print(i,end=' ')
    print()

##(10):-
temp=1
for i in range(1,11):
    for j in range(1,11):
      temp=temp+1
      print(temp,end=' ')
    print()

##ABCD(11):-
for i in range(65,70):
    x=chr(i)
    for j in range(65,70):
        if(i>=j):
            print(x,end=' ')
    print()
