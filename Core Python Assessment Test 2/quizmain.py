import constant
import mastermenu
import crackermenu

while True:
    print(constant.initialMessage)
    role = input(constant.enterRole)

    if role == "1" or role == "2":
        if role == "1":
            masterMenuOutput = mastermenu.startMasterMenu() 
            if masterMenuOutput == 1:
                continue
            elif masterMenuOutput == 2:
                break
        else:
            crackerMenuOutput = crackermenu.startCrackerMenu()
            if crackerMenuOutput == 1:
                continue
            elif crackerMenuOutput == 2:
                break
    
    else:
        print(constant.validInput)
        continue

    