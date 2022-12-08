n=input("enter the month:")
if n=="february":
    print(n,"is 28 or 29 days")
elif n in("april","june","september","november"):
    print(n,"is 30 days")
elif n in("januvary","march","may","july","aguest","october","december"):
    print(n,"is 31 days")
else:
    print("invalid data")
