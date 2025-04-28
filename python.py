price=0
print("Hello sir ")
print("welcome to our restaurant")
print("here's menu")
print("pizza          ₹99")
print("sandwich       ₹70")
print("salad          ₹80")
print("coffe          ₹20")

def cost(food):
    global price
    if food=="pizza":
        price=price+99
        
    elif food=="sandwich":
        price=price+70
    elif food=="salad":
        price=price+80
    else:
        price=price+20
    return price

food1=input("Enter what you would like to eat and we will serve it ")
cost1=cost(food1)
repeat=input("would youu like to order something more")
if repeat=="yes":
    rp=input("what would you like me to add")
    cost2=cost(rp)
    print(cost2)
    print("THANK YOU SIR")
else:
    print(cost1)
    print("THANK YOU SIR")

