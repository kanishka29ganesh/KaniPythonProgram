x=int(input('Enter row value'))
y=int(input('Enter a column value'))

a=[]

for i in range(x):
    a.append([])

    for j in range(y):
        temp=int(input('Enter number'))
        a[i].append(temp)
        
print(a)


b=[]

for i in range(x):
    b.append([])

    for j in range(y):
        temp=int(input('Enter number'))
        b[i].append(temp)
        
print(b)


for i in range(x):
    for j in range(y):
        temp=a[i][j]+b[i][j]
        print(temp,end=" ")
    print()


