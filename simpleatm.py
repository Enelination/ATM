def main():
    pinCode = ["1234", "1999", "2424", "1985",
               "5555"]  # data of the account holders
    accountHoldersName = ["enel", "kofi",
                          "Ama", "Bessy", "Theo"]
    accountNumber = ['1353', '199281', "182838", "185597", "667432"]
    balance = [567000, 21873, 2341871, 275638, 91820]

    flag = False
    for i in range(0, 999999999):  # so the loop runs almost infinit many times
        print("""
    \t\t=== Welcome To EnelTech ATM System ===
""")
        inputName = input("Enter Your Name: ")
        inputName = inputName.lower()
        # if pin is wrong it will be use as this is assigned before referance.
        inputPin = 0000
        # if pin is wrong it will be use as this is assigned before referance.
        index = 0
        for name in accountHoldersName:
            count = 0
            if name == inputName:
                # index of anme is stored and if the pin of that index is same user will be given access to the account.
                index = count
                inputPin = input("\nEnter Pin Number: ")
            count += 1

        if inputPin == pinCode[index]:
            flag = True
        else:
            print("Invalid data.")
            flag = False
            continue
        if flag == True:
            print("\nYour account number is: ", accountNumber[index])
            print("Your account balance is: GHS.", balance[index])
            drawOrDeposite = input(
                "\nDo you want to draw or deposit cash (draw/deposite/no): ")
            if drawOrDeposite == "draw":
                amount = input("\nEnter the amount you want to draw: ")
                try:  # Exception handling
                    amount = int(amount)
                    if amount > balance[index]:
                        raise
                except:
                    print("invalid amount.")
                    continue
                # subtracting the drawed amount.
                remainingBalalnce = balance[index] - amount
                # removing the old ammount from the list and adding the new list after draw.
                balance.remove(balance[index])
                balance.insert(index, remainingBalalnce)
                availableBalance = print(
                    "\nYour available balance is: ", remainingBalalnce)
            elif drawOrDeposite == "deposite":
                amount = input("Enter the amount you want to deposite: ")
                try:
                    amount = int(amount)
                    if amount > balance[index]:
                        raise
                except:
                    print("invalid amount.")
                    continue
                # adding the deposited amount.
                remainingBalalnce = balance[index] + amount
                # removing the old ammount from the list and adding the new list after draw.
                balance.remove(balance[index])
                balance.insert(index, remainingBalalnce)
                availableBalance = print(
                    f"Your available balance is GHS {remainingBalalnce}")
            print("\n\nThank you for using EnelTech ")


main()
