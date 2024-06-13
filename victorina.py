print("Добро пожаловать на викторину!")
print("Ответь на следующие вопросы:")

score = 0
questions = ["Как зовут друга чебурашки?","Какая страна самая большая?","Кого называют «царём зверей»?","С какого месяца начинается зима?"
, "Первый месяц лето?"
]

answers = ["Гена",
                 "Россия",
                 "Льва" ,
                 "Декабрь",
                 "Июнь"
 ]

print(questions[0])
user_input = input("Введите свой ответ: ")
if user_input.lower() == answers[0].lower():
    print("Правильно!")
    score +=1
else:
    print("Неправильно!")

print(questions[1])
user_input1 = input("Введите свой ответ: ")
if user_input1.lower() == answers[1].lower():
    print("Правильно!")
    score +=1
else:
    print("Неправильно!")

print(questions[2])
user_input2 = input("Введите свой ответ: ")
if user_input2.lower() == answers[2].lower():
    print("Правильно!")
    score +=1
else:
    print("Неправильно!")

print(questions[3])
user_input3 = input("Введите свой ответ: ")
if user_input3.lower() == answers[3].lower():
    print("Правильно!")
    score +=1
else:
    print("Неправильно!")

print(questions[4])
user_input4 = input("Введите свой ответ: ")
if user_input4.lower() == answers[4].lower():
    print("Правильно!")
    score +=1
else:
    print("Неправильно!")
print("Ваши баллы-",score)