##Eligble to vote(1):-
age=int(input('Enter your age'))
if(age>0 and age<=100):
    if(age>=18):
        print('You are eligible to vote')
    else:
        print('You are not eligible to vote')
else:
    print('Invalid Input')


##Finding leap year with century and non-century with elif(2):-
year=int(input('Enter a year'))
print('Year','=',year)
if(year%100==0):
    if(year%400==0):
        print('It is a leap year and a century year')
    else:
        print('It is not a leap year but a century year')
elif(year%4==0):
    print('It is a leap year and a non century year')
else:
    print('It is not a leap year but a non century year')


##Finding leap year with century and non century with else(3):-
year=int(input('Enter a year'))
print('Year','=',year)
if(year%100==0):
    if(year%400==0):
        print('It is a leap year and a century year')
    else:
        print('It is not a leap year but a century year')
else:
    if(year%4==0):
        print('It is a leap year and a non century year')
    else:
        print('It is not a leap year but a non century year')
