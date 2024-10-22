# Fornito da DCS - Center  &  DCS - Developer

import json
import os

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.data = None
        self.load_database()

    def load_database(self):
        """Carica il database dal file JSON."""
        if not os.path.exists(self.db_path):
            raise FileNotFoundError(f"Il file del database {self.db_path} non esiste.")
        
        with open(self.db_path, 'r') as file:
            self.data = json.load(file)

    def get_data(self):
        """Restituisce i dati caricati dal database."""
        if self.data is None:
            raise Exception("Il database non è stato caricato correttamente.")
        return self.data

    def add_entry(self, category, topic, description):
        """Aggiunge una nuova voce al database."""
        if category not in self.data:
            self.data[category] = {}
        self.data[category][topic] = {'description': description}

    def remove_entry(self, category, topic):
        """Rimuove una voce dal database."""
        if category in self.data and topic in self.data[category]:
            del self.data[category][topic]

    def save_database(self):
        """Salva le modifiche apportate al database."""
        with open(self.db_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def search_category(self, category):
        """Restituisce tutti i topic disponibili per una data categoria."""
        if category in self.data:
            return list(self.data[category].keys())
        else:
            return []

    def search_description(self, category, topic):
        """Restituisce la descrizione per una categoria e un argomento specifici."""
        if category in self.data and topic in self.data[category]:
            return self.data[category][topic]['description']
        else:
            return None
