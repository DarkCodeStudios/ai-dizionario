# main.py

# Fornito da DCS - Center  &  DCS - Developer

from driver.question_driver import get_user_question
from driver.answer_driver import AnswerDriver

def main():
    db_path = 'src/database.json'
    unanswered_path = 'src/unanswered_questions.json'
    answer_driver = AnswerDriver(db_path, unanswered_path)
    
    print("DCS - Search Engine , cerca qualsiasi parola con nostro motore di ricerca. (Ricerca prese da Google & Wikipedia)")

    while True:
        question = get_user_question()
        if question.lower() == 'exit':
            break

        response = answer_driver.get_response(question)
        print("Risultato:", response)

if __name__ == "__main__":
    main()
