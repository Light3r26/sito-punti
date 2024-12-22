# Guida all'uso del sito dei punti

## Introduzione
Questa guida ti aiuterà a configurare e utilizzare il sito dei punti. Si presume che tu abbia familiarità con Git/GitHub, Python e i database. Se non conosci questi strumenti, ti consigliamo di acquisire una conoscenza di base prima di procedere.

---

## 1. Clonare la repository e installare le librerie

Dopo aver clonato la repository, è necessario installare le librerie richieste. Si consiglia di utilizzare un ambiente virtuale Python per una gestione più pulita delle dipendenze. Tuttavia, se non sai cosa sia un ambiente virtuale o preferisci evitare complicazioni, puoi installare le librerie globalmente.
QUESTI PASSAGGI SONO TESTATI SOLO PER LA VERSIONE DI PYTHON 3.11.4,VERSIONI SUCCESSIVE NON SONO GARANTITE DI FUNZIONARE
Segui i passaggi qui sotto:

- **Per configurare un ambiente virtuale:** Le librerie sono elencate nel file `requirements.txt`. Puoi configurare un ambiente virtuale e installarle con i seguenti comandi:
  ```bash
  python3 -m venv env
  source env/bin/activate  # Per macOS/Linux
  .\env\Scripts\activate  # Per Windows
  pip install -r requirements.txt
  ```

- **Per installazione globale:** Usa uno dei due script inclusi nella repository:
  - **Windows:** Esegui il file [setup.bat](../../setup.bat).
  - **macOS/Linux:** Esegui il file [setup.sh](../../setup.sh).

Se riscontri problemi, controlla la versione di `Werkzeug`, che dovrebbe essere `2.2.2`. Versioni non compatibili possono causare errori.

---

## 1.5. Configurare una secret key

La secret key è utilizzata per la crittografia dei dati trasmessi. Se stai solo sperimentando o testando l'applicazione, puoi saltare questo passaggio. Altrimenti, procedi così:

1. Apri il file [secret_token.txt](../../secrets/secret_token.txt).
2. Inserisci un valore casuale o generato tramite un tool di creazione token sicuri.

---

## 2. Avviare il sito

Per avviare il sito, esegui il seguente comando nella directory principale della repository:
```bash
python3 main.py
```

Questo comando avvierà il server locale. Ora puoi accedere alle pagine pubbliche del sito tramite il browser. Per accedere alle funzionalità riservate, come la gestione dei punti, è necessario configurare un account amministratore.

---

## 2.5. Configurare le credenziali di default

Per accedere alla pagina **admin**, è necessario un account amministratore. Segui questi passaggi per configurarne uno:

1. Accedi alla pagina `/init_starter_admin` nel tuo browser.
2. Modifica il file [secret_starter_admin_password.txt](../../secrets/secret_starter_admin_password.txt) per impostare una password.
   - **Nota:** Se il campo password è vuoto, non sarà possibile creare l'account.
3. L'operazione creerà un account con email `s-admin.starter@isiskeynes.it`.

**Importante:** Dopo la creazione dell'account, il file `secret_starter_admin_password` verrà eliminato automaticamente. Assicurati di ricordare la password a meno che tu non voglia reimpostare il database.

---

## 3. Accesso e utilizzo delle funzionalità admin

Ora puoi accedere al sito con l'account amministratore appena creato. Dopo il login, avrai accesso alla pagina **admin**, dove potrai:

- Caricare file Excel per aggiornare i dati.
- Modificare i punti degli utenti.
- Visualizzare i punti di tutti gli utenti.

---

## Altre informazioni importanti

### Gestione dei punti e creazione di nuovi account

Per modificare i punti o aggiungere nuovi account non amministrativi, è necessario caricare un file Excel formattato correttamente. Consulta il [formato specifico](./formato_excel.md) per verificare che il file sia compatibile.

### Risorse future

Saranno resi disponibili:
- File di esempio per il database.
- Modelli Excel precompilati per facilitare il testing e l'importazione dei dati.


