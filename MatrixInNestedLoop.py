x=int(input('Enter row value'))
y=int(input('Enter a column value'))
a=[]
for i in range(x):
    a.append([])

    for j in range(y):
        temp=int(input('Enter number'))
        a[i].append(temp)
        print()
print(a)
