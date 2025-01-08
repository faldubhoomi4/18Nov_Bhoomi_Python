import constant

questionList = [
    {
    constant.key_id:1,
    constant.key_question:"Who is prime minister of India ?",
    constant.key_option:{
        constant.key_option1:"Rahul Gandhi",
        constant.key_option2:"Narendra Modi" 
        },
    constant.key_rightanswer:"Narendra Modi" 
    },
    {
    constant.key_id:2,
    constant.key_question:"Who developed C language ?",
    constant.key_option:{
        constant.key_option1:"Dennis Ritchie",
        constant.key_option2:"Andy Rubin" 
        },
    constant.key_rightanswer:"Dennis Ritchie" 
    },
    ]

def addDetailsInDictionary(id,question,optionList,rightAnswer):
    newDictionary = {
    constant.key_id:id,
    constant.key_question:question,
    constant.key_option:{
        constant.key_option1:optionList[0],
        constant.key_option2:optionList[1] 
        } ,
    constant.key_rightanswer:rightAnswer 
    }

    questionList.append(newDictionary)