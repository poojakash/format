#linear search
POS = -1
def search(list, n):

    for i in range(len(list)):
        globals()['POS'] = i+1
        if list[i] == n:
            print("found",POS)
            break
    else:
        print("Not found")

n= int(input("enter the key="))

list=[45,82,96,78,36]

search(list,n)
