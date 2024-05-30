## to draw a pyramid pattern
rows = input("enter rows: ")
j=1
k = 5+0j
print(type(k))
print(int(k))

if rows.isnumeric():
    rows=int(rows)
    for i in range(rows,0,-1):
        print(' '*i+' *'*(rows-i+1))
        j+=1
        if j>rows:
            print(' *'*j)
   
    for i in range(0,rows):
        print(' '*i+' '+' *'*(rows-i))
        
else:
    print('invalid rows')
