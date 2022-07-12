x = [2,6,8,9,5]
for j in range(len(x)):

    for i in range(len(x)-1):
        if x[i]>x[i+1]:
            x[i],x[i+1] = x[i+1],x[i]
print(x)