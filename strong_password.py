# a=int(input("enter the number:"))
# b=int(input("enter the second number:"))
# if a>0 and b>0:
#     c=a+b
#     if c>=15 and c<=20:
#         print("20")
#     else:
#         print("nonting")

a=int(input("enter the number:"))
b=int(input("enter the second number:"))
if a>=0 and b>=0:
    c=a+b
    d=15
    e=20
    while d<=e:
        if c>=d and c<=e:
            print("20")
        else:
            print("nothing")
        break