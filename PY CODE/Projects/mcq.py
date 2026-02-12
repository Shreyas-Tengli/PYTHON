print("HOW MUCH DO YOU KNOW ME")
print("--Level EASY --> HARD--")
questions=(("Which school I studied in?"),
           ("Which is favourite food to eat?"),
           ("What is my most favourite season?"),
           ("What colour do i like? "),
           ("What car brand do i like the most"))
options=(("A. CPEMS","B. SBR","C. APS","D. Gurukul"),
         ("A. Pizza","B. Burger","C. Home Food","D. YOU<3 "),
         ("A. Summer","B. Winter","C. Rainy ","D. Autum"),
         ("A. White","B. Black","C. Biege","D. Blue"),
         ("A. AUDI","B. MERCEDES","C. BMW","D. ROYLS ROYCE"))
answers=("C","D","A","B","C")
guesses=[]
score=0
question_num=0

for question in questions:
    print("--------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Enter(A,B,C,D):").upper()
    guesses.append(guess)
    if guess== answers[question_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!!")
        print(f"The correct answer is {answers[question_num]}")
    question_num+=1
print("---------------------------------------------")
print("-------------------RESULTS-------------------")
print("---------------------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

