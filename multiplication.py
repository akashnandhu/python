def mul(x,y) :
    if y==0 :
        return
    mul(x,y-1)

    print(y," * ",x," = ", y*x)
max=10
mul(2,max)