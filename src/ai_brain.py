# Fornito da DCS - Center  &  DCS - Developer

import json
import requests
import wikipediaapi
from bs4 import BeautifulSoup

class AIBrain:
    def __init__(self, db_path, unanswered_path):
        self.db_path = db_path
        self.unanswered_path = unanswered_path
        
        self.wiki_wiki = wikipediaapi.Wikipedia(
            language='it',
            extract_format=wikipediaapi.ExtractFormat.WIKI,
            user_agent='MyQuestionAnsweringSystem/1.0 (https://example.com; support@example.com)'
        )
        
        # Carica il database
        self.load_database()
        
        # Carica le domande non risolte
        self.unanswered_questions = self.load_unanswered_questions()

    def load_database(self):
        """Carica il database dal file JSON."""
        try:
            with open(self.db_path, 'r') as file:
                self.database = json.load(file)
                # Commentato per evitare di stampare il contenuto del database
                # print(f"Database caricato: {self.database}")  
                if not isinstance(self.database, dict):
                    raise ValueError("Il database deve essere un oggetto JSON.")
        except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
            print(f"Errore nel caricamento del database: {e}")  # Messaggio di errore solo se necessario
            self.database = {}

    def load_unanswered_questions(self):
        """Carica le domande senza risposta."""
        try:
            with open(self.unanswered_path, 'r') as file:
                content = file.read().strip()
                if content == "":
                    return {}  # Ritorna un dizionario vuoto se il file è vuoto
                return json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}  # In caso di errore, ritorna un dizionario vuoto

    def save_unanswered_question(self, question):
        """Salva una domanda non risolta."""
        if isinstance(self.unanswered_questions, dict):
            if question not in self.unanswered_questions:
                self.unanswered_questions[question] = None  # Usa None come valore temporaneo
                with open(self.unanswered_path, 'w') as file:
                    json.dump(self.unanswered_questions, file, indent=4)

    def save_question_to_db(self, question, answer):
        """Salva una nuova domanda e risposta nel database."""
        if question.lower() not in self.database:
            self.database[question.lower()] = {"description": answer}
            with open(self.db_path, 'w') as file:
                json.dump(self.database, file, indent=4)
            # Messaggio di conferma commentato
            # print(f"Domanda salvata nel database: {question}")  # Debugging

    def search_wikipedia(self, question):
        """Cerca la risposta su Wikipedia."""
        page = self.wiki_wiki.page(question)
        if page.exists():
            return page.text[:500]  # Restituisce i primi 500 caratteri della pagina
        return None

    def search_google(self, question):
        """Cerca la risposta su Google."""
        url = f"https://www.google.com/search?q={question}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            result = soup.find('div', class_='BNeawe iBp4i AP7Wnd')  # Trova la descrizione di risposta
            if result:
                return result.get_text()
        return None

    def think(self, question):
        """Prova a rispondere alla domanda cercando nel database, su Wikipedia o Google."""
        question = question.strip().lower()  # Normalizza la domanda
        # Prima cerca nel database
        if question in self.database:
            return self.database[question]["description"]

        # Se non trova nulla, salva la domanda come non risolta
        self.save_unanswered_question(question)

        # Cerca su Wikipedia
        wiki_response = self.search_wikipedia(question)
        if wiki_response:
            self.save_question_to_db(question, wiki_response)
            return f"Ho trovato queste informazioni su Wikipedia: {wiki_response}"

        # Se non trova nulla, cerca su Google
        google_response = self.search_google(question)
        if google_response:
            self.save_question_to_db(question, google_response)
            return f"Ho trovato queste informazioni su Google: {google_response}"

        return "Mi dispiace, non ho trovato una risposta."
