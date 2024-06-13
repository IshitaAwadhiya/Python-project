print("\n","*********WELCOME TO MY QUIZ GAME*********","\n")
questionBank = [
    {"text" : "The ability of one class to aquare methods and attribute of another class called?",
     "Answer":"A"},
    {"text":"Which of the following is a type of Inheritance?",
     "Answer":"D"},
    {"text":"What type of Inheritance has multiple subclasses to a single superclass?",
     "Answer":"C"},
    {"text":"What is the depth of multi-level Inheritance in python?",
     "Answer":"C"},
    {"text":"What does MRO stand for?","Answer":"B"}
]

options = [
    ["A. Inheritance","B. Abstraction","C. Polymorphism","D. Encapsulation"],
    ["A. Single","B. Double","C. Multiple","D. Both A&C"],
    ["A. Multiple Inheritance","B. Multi-level Inheritance","C. Hierarichal Inheritance","D. None of these"],
    ["A. Second level","B. Third level","Any level","D. None of the above"],
    ["A. Method Recursive Object","B. Method Resolution Order","C. Multiple Recursive Order","D. Maintenance Resolution Operation"]
]

score = 0
def check_ans(user_guess,correct_ans):
    if user_guess == correct_ans:
        return True
    else:
        return False

for questions_num in range(len(questionBank)):
    print("--------------------------------------")
    print(questionBank[questions_num]["text"])
    for i in options[questions_num]:
        print(i)
        
    guess = input("Choose the correct option:").upper()
    is_correct = check_ans(guess, questionBank[questions_num]["Answer"])

    if is_correct:
       print("CORRECT ANSWER..")
       score += 1
    else:
       print("INCORRECT ANSWER..")
       print(f"The correct Answer is {questionBank[questions_num]['Answer']}")
    print(f"Your Current score is {score}/{questions_num+1}")
print(f"You have given {score} correct answer")
print(f"YOur Score is {(score/len(questionBank))*100}%")