# Python Journey: Encryption 🔐

Salve e benvenuti nel mio deposito. Sono Tiziano! In questo periodo sto cercando di approfondire python e, per allenarmi, mi sono cimentato nel provare a scrivere due piccoli codici di crittografia, uno attraverso il metodo del cifrario di cesare, l'altro attraverso la manipolazione di bit con l'operatore XOR.


## 🛠️ Progetto: criptazione

Il repository è diviso in due fasi principali:

- **Cesar Cipher Code:** Questo è stato il mio primo approccio, ovvero l'utilizzo del metodo del cifrario di cesare. 
- **Advanced XOR cryptation:** Questo è stato il secondo approccio, ovvero l'uso dello XOR per manipolazione bitwise

### 🏛️ 1. Cesar Cipher Code (`cesar_cipher_code.py`)

In questo primo approccio, ho lavorato sulla sostituzione dei caratteri basata su un alfabeto fisso.
- **Logica:** Utilizza una formula lineare `(pos * 8 + 5*6) % 36`.
- **Analisi Matematica:** Ho documentato un comportamento ciclico di periodo 2 (Set Pari/Dispari). Applicando l'algoritmo due volte, il testo segue pattern prevedibili che ho analizzato durante il debugging.

### 🤖 Advanced XOR Encryption (`advanced_XOR_cryptation.py`)
In questo secondo approccio provo a scrivere un codice utilizzando un metodo di crittografia simmetrica usano l'operatore XOR
- **Tecnica:** Manipolazione bitwise tramite l'operatore XOR (`^`).
- **Gestione Chiave:** Implementazione di una chiave rotante tramite aritmetica modulare, permettendo di usare passphrases di qualsiasi lunghezza (anche un'intera ricetta siciliana!).
- **Robustezza:** Uso di decoratori per la sanitizzazione dei dati e gestione dei tipi (stringhe/liste).

---
Progetto realizzato da **TMSapphir** durante il percorso di studio Python. 😊👋