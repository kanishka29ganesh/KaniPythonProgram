####(1):-
##a='Hello'
##print(len(a))
##print(a[1])
##
####(2):-
##b='Ocean Acadamy'
##print(len(b))
##print(b[9],b[0])
##
####(3):-
##c='kanishka'
##print(len(c))
##(c[0])=='K'
##print(c[0])
##
####(4):-
##r=' Python Programme'
##print(len(r))
##for i in range(0,len(r)):
##    print(r[i])
##
####(5):-
##k=' Ocean Acadamy'
##print(len(k))
##for i in range(0,len(k)):
##    print(k[i])
##
####With Range(6):-
##a='Hello'
##for i in range(0,len(a)):
##    print(a[i])
##
####Without Range(7):-
##a='Hello'
##for i in a:
##    print(i)
##
####String Slicing(8):-
##a='Ocean Acadmey'
##print(a[0:5:1])
##print(a[6:13:1])
##
####String Slicing(9):-
##b='123456789'
##print(b[0:9:2])
##print(b[0:9:1])
####
####string slicing(10):-
##a='Kanishka Ganesh'
##print(len(a))
##for i in a:
##    print(i)
##print(a[0:16:2])
####
####Finding length of given without len(11):-
##a=int(input('Enter a string'))

##
####adding ly and ing(12):-
##a=input('Enter a word')
##z=int(len(a))
##y=int(len(a)-1)
##x=int(len(a)-2)
##q=int(len(a)-3)
##
##s=(a[q:z])
##
##if(s=='ing'):
##    pass
##else:
##    print(a+'ing')
##
####aeiou(13):-
##num=input('Enter a word')
##
##A=int(num.count('a'))
##E=int(num.count('e'))
##I=int(num.count('i'))
##O=int(num.count('o'))
##U=int(num.count('u'))
##
##print(A+E+I+O+U)

####index value(14):-
##a=input('Enter a value')
##b=a+'|'
##
##print('The number of characters',b.index('|'))
##
####(15):-
##a=input('Enter a value')
##if(len(a)%2==0):
##    print('True')
##else:
##    print('False')
##
####(16):-
##a=input('Enter a value')
##m=a[0]
##l=a[len(a)-1]
##print(m+l)
##
####(17):-
##string=input('Enter a string')
##x=string[0]
##y=string[-1]
##print(x+y)

##(18):-
a=int(input('Enter a stop value'))
for j in range(a):
    b=input('enter a value')
    x=0
    for i in b:
        y=len(i)-1
        z=i[0]
        n=i[y]

