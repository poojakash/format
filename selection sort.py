def sort(x):
    x = [5,6,8,5,9]
for i in range(len(x)):
    minpos = i
    for j in range(i,len(x)):
        if x[j]<x[minpos]:
            minpos = j
            temp=x[i]
            x[i]=x[minpos]
            x[minpos]=temp
sort(x)
print(x)

