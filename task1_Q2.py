x=int(input("how many Banking operations do you want to do? "))
balance = 0
for i in range(x) :
    increase = float(input("how much money do you want to put in your account :"))
    decrease = float(input("how much money do you want to cash out :"))
    balance += (increase - decrease)

    print("your balance is",balance)
