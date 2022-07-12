#place holder is a telplate for any typ of data to fit in it

x= "Hello %s, you are invited to my birthday party"
print(x%("Pooja"))
y=["Akash","Pooja"]
for i in y:
    print(x%(i))

#if we want to add name and age

x = "Name is %s,and Age is %d"
print(x%("Pooja",14))

#if we want to add two names

x = "Hello %s %s, you are invited to my birthday party"
print(x%("Pooja","Bhatakande"))

