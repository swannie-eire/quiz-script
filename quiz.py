from random import randrange
import copy

exam = 'EXAMFILE-NAME'

# Using readline()
file1 = open(exam, 'r')
count = 0
some_string = ""

read_questions = []
quiz_questions = []
result = []

while True:
    count += 1

    # Get next line from file
    line = file1.readline()

    # if line is empty
    # end of file is reached
    if not line:
        break
    #print("Line{}: {}".format(count, line.strip()))
    some_string + line.strip()

file1.close()



with open(exam) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

full_question = {
    "question_number": "",
    "question": "",
    "choices": {"a": "", "b": "", "c": "", "d": ""},
    "answer": "",
    "user_answer": ""
}
answer = ""
question = ""


def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

for line in content:
    if line.__contains__("QUESTION"):
        full_question['question_number'] = line
    elif line.__contains__("Correct Answer: "):
        new = line.replace('Correct Answer: ','')
        for char in new:
            answer += char
            #print(full_question)
        full_question['question'] = question
        full_question['answer'] = answer
        read_questions.append(copy.deepcopy(full_question))
        question = ""
        answer = ""
        if 'e' in full_question['choices']:
            del full_question['choices']['e']
    elif not line.startswith("A. ") and not line.startswith("B. ") and not line.startswith("C. ") and not line.startswith("D. ") and not line.startswith("E. ") and not line.startswith("F. "):
        question += line
    elif line.startswith("A."):
        full_question['choices']['a'] = line[3:]
    elif line.startswith("B."):
        full_question['choices']['b'] = line[3:]
    elif line.startswith("C."):
        full_question['choices']['c'] = line[3:]
    elif line.startswith("D."):
        full_question['choices']['d'] = line[3:]
    elif line.startswith("E."):
        full_question['choices']['e'] = line[3:]
    elif line.startswith("F."):
        full_question['choices']['f'] = line[3:]

def print_result():
    print(len(result))
    l = list(result)
    print("Number Of correct Answers = " + str(l.count(True)))
    print("Percent result = " + str(round((l.count(True) / len(result) * 100), 2))  + "%")
    for i in range(len(result)):
        if not result[i]:
            print(quiz_questions[i]['question_number'])
            print(quiz_questions[i]['question'])
            #print(quiz_questions[i]['answer'])
            if len(quiz_questions[i]['answer']) == 1:
                print("Correct Answer = " + quiz_questions[i]['answer'] + ": " + str(quiz_questions[i]['choices'][quiz_questions[i]['answer'].lower()]))
                print("Your Wrong Answer = " + str(quiz_questions[i]['user_answer']) + ": " + str(quiz_questions[i]['choices'][quiz_questions[i]['user_answer'].lower()]))
            else:
                for char in str(quiz_questions[i]['answer']):
                    print("Correct Answer = " + char + ": " + str(quiz_questions[i]['choices'][char.lower()]))
                for char in str(quiz_questions[i]['user_answer']):
                    test = quiz_questions[i]['choices']
                    if char.lower() in quiz_questions[i]['choices']:
                        print("Your Wrong Answer = " + char + ": " + str(quiz_questions[i]['choices'][char.lower()]))
                    else:
                        print("Your Wrong Answer = " + char)


def char_in_ans(user_input, answer):
    for char in user_input:
        if char.lower() not in str(q['answer']).lower():
            #print(char)
            return False

    return True

number_of_questions = int(input("how many questions you want?\n"))

while number_of_questions != 0:
    random_number = randrange(len(read_questions))
    quiz_questions.append(copy.deepcopy(read_questions[random_number]))
    read_questions.pop(random_number)
    number_of_questions -= 1




count = 1
for q in quiz_questions:
    print("\n" + "Question " + str(count) + " of " + str(len(quiz_questions)))
    print
    print(q['question_number'])
    print(q['question'].replace(". ",". \n"))
    if q['question'].__contains__("Choose two"):
        print("Choose two".upper())
    for key, value in q['choices'].items():
        print(key.upper(), ' : ', value)
    while True:
        user_answer = input("Pick an answer from " + str(list(q['choices'].keys())) + " :")
        if len(user_answer) != 1 and len(user_answer) == len(q['answer']):
            in_answers = False
            for i in user_answer:
                print(i)
                if i.lower() not in q['choices'].keys():
                    print("\nNot an appropriate choice.")
                    break
                else:
                    in_answers = True
            if in_answers:
                break
        elif user_answer.lower() not in q['choices'].keys() or len(user_answer) != len(q['answer']):
            print("\nNot an appropriate choice.")
        else:
            break
    #user_answer = input("Please enter a answer:\n")
    q['user_answer'] = user_answer
    if user_answer.lower() == str(q['answer']).lower():
        result.append(True)
    elif len(user_answer.lower()) != len(str(q['answer']).lower()):
        result.append(False)
    else:
        result.append(char_in_ans(user_answer, str(q['answer']).lower()))
    count += 1



print_result()