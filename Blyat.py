print("Välkommen till pappa alfreds spargris")

balance = 10000

option = 0

print("press 1 for balance")
print("press 2 for withrawal")
print("press 3 to deposit")
print("perss 4 to exit")

while option != 4:
    
    try:
        option = int(input("Choose an option to advance further: "))
    except:
        print("You must choose a number between 1 and 4!")
    
    if option == 1:
        print(balance)
    elif option == 2:
        withraw = int(input("type the amount of which you want to withraw:"))
        balance = balance - withraw
        print ("your current balance", balance)
    elif option == 3:
        deposit = int(input("type the amount of which you want to deposit:"))
        balance = balance + deposit
        print ("your currenct balance", balance)
    elif option == 4:
        print("Till next time")

