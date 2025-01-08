import constant
import common

def startMasterMenu() -> int:
    print(constant.masterMenu)
    userMenuSelection = input(constant.menuOperationSelaction)

    if userMenuSelection == "1" or userMenuSelection == "2" or userMenuSelection == "3":
        match userMenuSelection:
            case "1" :
                addQuestion()
            case "2" :
                viewQuestion()
            case _ :
                #   userMenuSelection == 3
                deleteQuestion()
    elif userMenuSelection == "4":
        exit()
    else:
        print(constant.validInput)
        #   continue
        return 1
    
    return 0

def addQuestion() :
    question = input(constant.enterQuestion)
    optionOne = input(constant.enterOpOne)
    optionTwo = input(constant.enterOpTwo)
    rightAnswer = input(constant.enterRightAnswer)

    common.addDetailsInDictionary(len(common.questionList) + 1, question, (optionOne, optionTwo), rightAnswer)
    print(constant.questionSuccessfullyAdded)

    
    

def viewQuestion() :
    for i in range(0, len(common.questionList)):
        print(f"{i+1}) {common.questionList[i][constant.key_question]}")
        print(f"A : {common.questionList[i][constant.key_option][constant.key_option1]}")
        print(f"B : {common.questionList[i][constant.key_option][constant.key_option2]}")
        print(f"RIGHT ANS : {common.questionList[i][constant.key_rightanswer]}")

    
    
    
def deleteQuestion() :
    questionId = int(input(constant.enterDeleteQuestionId))
    userConfirmation = input(constant.deleteQuestionConfirmation)

    if userConfirmation == "Y":
        for i in range(0,len(common.questionList)):
            if common.questionList[i][constant.key_id] == questionId:
                del common.questionList[i]
                print(constant.questionSuccessfullyDeleted)
                break

    