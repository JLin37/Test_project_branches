def calTotal(price, fees):
    return (price * (1+fees))
    print("hi everyone")

def calNewPrice(budget, fees):
    return (budget/(1+fees))

budget = int(input("tell us your desired budget: "))

price = 85
fees = 0.15

total = calTotal(price, fees)
print(total)

if total < budget:
    print("you are under budget")
elif total == budget:
    print("you are right on budget")
else:
    print("you are over budget")
    newPrice = calNewPrice(budget, fees)
    print(f"your new price based on your budget is: {newPrice}")
    print(f"your new total value is: {calTotal(newPrice, fees)}")