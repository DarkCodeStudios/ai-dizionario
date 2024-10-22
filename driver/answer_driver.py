# driver/answer_driver.py

# Fornito da DCS - Center  &  DCS - Developer

from src.question_answer import QuestionAnswerSystem

class AnswerDriver:
    def __init__(self, db_path, unanswered_path):
        self.qa_system = QuestionAnswerSystem(db_path, unanswered_path)

    def get_response(self, question):
        """Restituisce la risposta alla domanda fornita."""
        return self.qa_system.ask(question)
