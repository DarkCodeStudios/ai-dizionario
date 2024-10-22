# Fornito da DCS - Center  &  DCS - Developer

from src.ai_brain import AIBrain
from src.database_manager import DatabaseManager

class QuestionAnswerSystem:
    def __init__(self, db_path, unanswered_path):
        self.db_manager = DatabaseManager(db_path)
        self.brain = AIBrain(db_path, unanswered_path)

    def ask(self, question):
        """Riceve una domanda e chiede al 'cervello' di fornire una risposta."""
        response = self.brain.think(question)
        return response

    def provide_answer(self, question, category, topic, description):
        """Permette di aggiungere una risposta per una domanda non risolta."""
        self.db_manager.add_entry(category, topic, description)
        self.db_manager.save_database()
        print(f"Nuova parola aggiunta al database: [{category}] {topic} - {description}")
