#EasyBot
#By lintuxos

try:
    questions = ["What's your name?"]
    answers = ["My name is EasyBot!"]

    def elementNumber(a, b):
        counter = 0
        for x in a:
            if b == x:
                return counter
            counter += 1
        return None

    print("Start a conversation!")
    while True:
        x = input()
        if x in questions:
            print(answers[elementNumber(questions, x)])
        else:
            print("Unfortunately, I can't answer that yet. What would you say to that?")
            y = input()
            questions.append(x)
            answers.append(y)

except:
    print("Good bye!")