# Documentazione per il sistema di ricerca di parole (dizionario)

## Content:

1. [Introduzione](#introduzione)
2. [Requisiti](#requisiti)
3. [Installazione](#installazione)
4. [Struttura del Progetto](#struttura-del-progetto)
5. [Utilizzo](#utilizzo)
6. [Driver](#driver)
   - [Driver delle Domande](#driver-delle-domande)
   - [Driver delle Risposte](#driver-delle-risposte)
   - [Driver del Database](#driver-del-database)
7. [Esempi di Utilizzo](#esempi-di-utilizzo)
8. [Contribuire](#contribuire)
9. [Licenza](#licenza)

## Introduzione

Questo sistema di intelligenza artificiale è progettato per rispondere a alle parole cercate dall'utente, cercando risposte all'interno di un database predefinito e, se necessario, attraverso ricerche online. Utilizza un'architettura modulare, consentendo di separare le diverse funzionalità in vari driver.

## Requisiti

- Python 3.6 o superiore
- Moduli Python:
  - `wikipedia-api`
  - `requests`
  
Puoi installare i requisiti necessari utilizzando il seguente comando:

```bash
pip install wikipedia-api requests
```

## Installazione

1. Clona il repository o scarica i file del progetto sul tuo computer.

2. Apri la cartella del progetto.

3. Assicurati che tutti i requisiti siano installati (vedi Requisiti).

4. Esegui il file ```main.py```:

```bash
python main.py
```

## Struttura del Progetto

```
├── doc
├── driver
│   ├── __init__.py
│   ├── question_driver.py
│   ├── answer_driver.py
│   └── database_driver.py
├── main.py
└── src
    ├── ai_brain.py
    ├── database.json
    ├── database_manager.py
    ├── __pycache__
    ├── question_answer.py
    └── unanswered_questions.json
```
- **doc/**: Cartella per la documentazione.

- **driver/**: Contiene i driver per gestire l'input e l'output del sistema.

- <a href="../main.py">**main.py**</a>: Il file principale che esegue il sistema.

- **src/**: Contiene la logica dell'intelligenza artificiale e i dati.

## Utilizzo

Dopo aver avviato il programma, il sistema ti chiederà di inserire una domanda. Puoi inserire qualsiasi domanda tu voglia e il sistema cercherà di fornire una risposta. Per uscire dal programma, digita ```exit```.

# Driver

## Driver delle Domande
-    ```driver/question_driver.py```: Gestisce l'input dell'utente.

Funzione principale:

-    ```get_user_question()```: Restituisce la domanda fornita dall'utente.

## Driver delle Risposte

-   ```driver/answer_driver.py```: Gestisce la logica per fornire risposte alle domande.

Classi principali:

-    ```AnswerDriver```: Interagisce con il sistema di domande e risposte per ottenere risposte.

## Driver del Database

- ```driver/database_driver.py```: (Opzionale) Puoi implementare qui funzioni per gestire le interazioni con il database.

## Esempi di Utilizzo

1. Esempio di ricerca:

```txt
Fai una ricerca (o digita 'exit' per uscire): cpu
```
Non bisogna scrivere una frase ma solo una parola come ad esempiuo "```cpu```" invece che "```Cos'è una CPU```"

2. Esempio risposta:

```
Risposta: La CPU (Central Processing Unit) è l'unità centrale di elaborazione di un computer...
```

## Contribuire

Se desideri contribuire al progetto, sentiti libero di inviare un ```pull request``` o aprire un'```issue``` per discutere nuove funzionalità o miglioramenti.

## Lincenza

Questo progetto è rilasciato sotto la Licenza MIT. Per maggiori dettagli, consulta il file ```LICENSE```.