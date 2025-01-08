import constant
import common

def startCrackerMenu() -> int:
    print(constant.crackerMenu)
    userMenuSelection = input(constant.menuOperationSelaction)

    if userMenuSelection == "1" or userMenuSelection == "2":
        if userMenuSelection == "1":
            startQuiz()
        else:
            exit()
    else:
        print(constant.validInput)
        #   continue
        return 1
    
    return 0

def startQuiz():
    rightAnswerCount = 0
    for i in range(0, len(common.questionList)):
        print(f"{i+1}) {common.questionList[i][constant.key_question]}")
        print(f"A : {common.questionList[i][constant.key_option][constant.key_option1]}")
        print(f"B : {common.questionList[i][constant.key_option][constant.key_option2]}")

        userAnswer = input(constant.answer)
        if common.questionList[i][constant.key_rightanswer] == userAnswer:
            rightAnswerCount += 1
            
    name = input(constant.enterName)
    print(f"{name} you have scored {rightAnswerCount}/{len(common.questionList)} in this quiz.")
     
