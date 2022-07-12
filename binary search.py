#binary search
def bsearch(list, n):
    l=0
    u=len(list)-1

    while l<=u:
        mid = (l+u)//2

        if list[mid]==n:
            return True
        elif n<list[mid]:
            u=mid-1
        else:
            l=mid+1

    return False


list=[20,22,30,33,50,56]

n=33
if bsearch(list, n):
    print("found")
else:
    print("not")
