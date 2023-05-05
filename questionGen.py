
class Question :
    def __init__(self , question , answer ,option):
        self.question = question
        self.answer = answer
        self.option = option[0] + "\n" + option[1]+ "\n" + option[2] +"\n" + option[3]

    def ques(self) -> str:
        return self.question
    
    def opt(self) -> str:
        return self.option

    def answer(self) -> str:
        return self.answer
    





def gen():
    questions = []
    with open('questions.txt', 'r') as file:
        while True:
            lines = [file.readline().strip() for _ in range(6)]
            
            if not any(lines):
                # End of file or empty lines, break the loop
                break

            question = lines[0]
            options = lines[1:5]
            answer = options[int(lines[5])-1]

            q1 = Question(question=question , option=options , answer=answer)
            questions.append(q1)

    return questions


if __name__ == "__main__":
    q = gen()

    print(type(q[0].opt()))