def table(n,i=1):
    print(n*i)
    if i<10:
        table(n,i+1)   
table(12)

