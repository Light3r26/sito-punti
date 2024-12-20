# Come usare il sito dei punti
*premessa : questa guida e la documentazione in generale da per scontato che tu sia almeno un po' familia refamiliare con i concetti comuni di git/github python e database *

# 1 : Clone della repo e installazione delle librerie

Per prima cosa dopo aver clonato la repositoria avrai bisogno di installare le librerie necessarie.Se vuoi usare un ambiene virtuale python,la librerie sono segnate nel file requirements.txt,altrimenti,se non sai cosa e' un ambiente virtuale o vuoi installare le librerie in ambiente globale,puoi usare i 2 script per l'installazione automatica:
- Se sei su Windows runna il file [setup.bat](../../setup.bat)
- Se sei su Macos o Linux runna il file [setup.sh](../../setup.sh)

Con questa installazione automatica non ci dovrebbero essere problemi,ma se ne riscontri ti consigliamo di controllare la versione di Werkzeug (che dovrebbe essere 2.2.2) visto che abbiamo riscontrato dei problemi in alcune installazioni

# 1.5 : Impostare una secret key

Se non se troppo preoccupato della criptazione dei dati passati nell'applicazione allora puoi anche saltare questo passaggio,altrimenti,puoi modificare il token che si occupa della criptazione in questo file : [secret_token.txt]( ../../secrets/secret_token.txt).Puoi cambiarlo ad un valore arbitrario o randomico che ritieni opportuno
# 2 : Impostare le credenziali di default

L'unico modo per accedere alla pagina admin è un account admin,e per creare un account admin avrai prima bisogno di un account admin.Per questo collegandosi alla pagina /init_starter_admin è possibile creare un account admin con email s-admin.starter@isiskeynes.it e una password che dovrai impostare nel file [secret_starter_admin_password.txt](../../secrets/secret_starter_admin_password.txt).Se lasci vuota la password non potrai creare l'account.
Una volta create questo account volendo puoi anche cancellare il file secret_starter_admin_password se hai paura che qualcuno la possa vedere

# 3 : Finalmente si entra

Adesso puoi loggarti all'interno del sito con quel'account e accedere alla pagina admin dove potrari caricare file excel e modificare punti.




# Altre cose importanti

Se vuoi modificare punti o creare nuovi account che non siano admin,avrai bisogno di caricare un file excel secondo [questo](./formato_excel.md) formato così da creare un database iniziale con dei dati 
In futuro saranno resi disponibili dei file di esempio per il database e file excel per semplificare il processo di testing




