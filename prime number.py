for i in range(1,101):
    if i>1:
        for j in range(2,i-1):
            if i%j==0:
                break
        else:
            print("%d"%i,end=' ')