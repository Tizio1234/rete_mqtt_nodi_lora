# MQTT via LoRa

#### Questa e un'applicazione Python che permette l'uso di un protocollo simile all'MQTT via LoRa, questo e un diagramma di esempio di applicazione di questo progetto:

![](https://lh3.googleusercontent.com/5CI6gWBbk7qIJjPY_e6OluQtWEBhYAL518VgzD6JqNOsTEHCl1cap8uGMer4hBg3xz-DjbsWFMierUN-tOqOlfXV55JwAOAEZYUUjbdTiEDgCvZ5slOeNuL8FZ8mLSn-viCHXsmShjBA1V7lluxHCA2kJN4xMDQpv26nsnSxawqeXywMFsdOvT8acNhf8Dw41go6hwOhtDf9oBpEsRxNmnNb5Vt-_5Fawc3XDZ5RbzpMmK8zZCWhZCc0FWtmQJgP5cAFgZ4ppm-z_UxkBz_AZXbLXTJB-W2__IlNWgzhlpirsEbejSob4wO8czB7-YcQOzjNMTTKSc0ACtd1JSm7Ppq8Rb2ueajDuyhCRVUOYV92cIR4oTZQlUEZVJ5VAIjclFUFUwAAU09VuPApRaGJuE-RQCFh3tOTB-zlTse-w_2NmaJiExlIGFCiSzIOK01bLc_uBFakGk4-33kcZeVwKXTaLN828TYGSfHyxazkW1z7tiE1WTK0yEqIiBgVNN6g4cOf8N7QtvvnpasIFDn1whFbiCLCL-6q29Wh9R0AHSRgOzbPah9jz0oY0xUsa0OYAc2a4T9q7oQpZ5fDsEEnIZys45nsVm3n9ZVxFxX3pzW-qdfFc2IKSItHwuhKXbksMqSZPmqg4u2k55YULFCYGQowLEBUmVMIun9atHf6zAfzsJPdcUw3u6U7O94AFbPQlcr0iXuthdoN1pbkPIMICUDdXqM6G6G1H1rrFa5sudjTTVGyPjRftiatkT8Mb0SR6WmgyeFWV1bweB1NoaLWu0Rth2ZEvAUiAhI5KLYnhEAmoodBtm3IDZdbkuwdnFgkYaMasFxwWVnDXdjksxWwXMXgl2y6Tq9JjXLlWHQUhF1wkw3yrR0KepFbSYxow1ysDwc-NsIzrUbksWcJWv-9xWV8hqn-7x6wGv6DMs03pCeXb-4EFXHMxWWI7kJlJsiyxA1oX3a9v_rgoqzbaQ=w2492-h1878-s-no?authuser=0)

#### Tutta la struttura e formata da tre parti principali:

- #### Raspberry pi 4: ha il compito di svolgere le funzioni principali di un broker mqtt

- #### Esp32 Master: ha il compito di far passare messaggi fra i nodi della rete LoRa e Raspberry e viceversa con una porta seriale

- #### Nodi(Esp32 o qualsiasi altra scheda in grado di trasmettere attraverso il protocollo LoRa): clienti del broker mqtt

#### Quest'applicazione in particolare si occupa della prima parte(Raspberry pi 4), essa e il cosiddetto broker, si occupa delle funzioni principali di un broker MQTT, al momento esse sono:

- #### Gestire richieste di iscrizione ad un argomento

- #### Gestire richieste di disiscrizione ad un argomento

- #### Gestire richieste di pubblicazione di un messaggio su un argomento

#### Strumenti usati e la loro documentazione:

- [3.9.16 Documentation](https://docs.python.org/3.9/)

- [re — Regular expression operations &#8212; Python 3.9.16 documentation](https://docs.python.org/3.9/library/re.html)

- [Django documentation | Django documentation | Django](https://docs.djangoproject.com/en/4.2/)

- [Welcome to pySerial’s documentation &mdash; pySerial 3.4 documentation](https://pyserial.readthedocs.io/en/latest/)

#### Questo e l'albero delle cartelle e i files che ci interessano:

.

├── compose.py

├── db.sqlite3

├── decompose.py

├── funzioni_logica_mqtt.py

├── gestione_schede_lora_1

│   └── settings.py

├── main.py

├── manage.py

├── mqtt_lora

│   ├── admin.py

│   └── models.py

└── regex_formats.py

#### In questo albero possiamo identificare vari files che corrispondono ai tre blocchi indicati nel diagramma:

- #### La struttura del database Django e` contenuta nel file [models.py](./mqtt_lora/models.py):
  
  #### Qui vengono dichiarati tre modelli, che ereditano dalla classe models.Model interna al modulo python django in se:
  
  - #### DataBaseMessage:
    
    #### Questo tipo di oggetto non e necessario al funzionamento dell'applicazione standalone, ma in caso si volessero visualizzare i messaggi scambiati in questa infrastuttura, sara sempre utile
  
  - #### Scheda:
    
    #### Questo oggetto rappresenta un singolo nodo o scheda, ogni scheda ha due bytes di addresso unici nello stesso canale della stessa infrastuttura, altrimenti si puo creare della confusione, fra schede e topics c'e una relazione molti a molti, vuol dire che una scheda puo essere iscritta a piu di un topic e un topic puo avere piu di una scheda iscritta ad esso
  
  - #### Topic:
    
    #### Questo tipo di oggetto rappresenta un argomento del broker mqtt, in particolare esso tiene il nome dell'argomento e le varie Schede iscritte ad esso

- #### La struttura del blocco "messaggi seriale" si puo` trovare nei files [decompose.py](./decompose.py) e [regex_formats.py](./regex_formats.py):
  
  - #### Nel file regex_formats.py sono presenti le varies stringhe di interpretazione dei messaggi arrivati dall'esp32 per scomporre i messaggi, per fare cio viene usato il modulo python re che premette di interpretare stringhe secondo espressioni regolari(regex)
  
  - #### Nel file decompose.py sono presenti le varie funzioni che interpretano i vari tipi di messaggi che usano i formati dichiarati in regex_formats

- #### La struttura del blocco "logica mqtt" si trova nei files [funzioni_logica_mqtt.py](./funzioni_logica_mqtt.py) e [main.py](./main.py):
  
  - #### Il file funzioni_logica_mqtt dichiara varie funzioni importate da main.py che servono ad applicare la logica del broker mqtt a dei cambiamenti sul database
  
  - #### Invece il file main.py e il "flusso principale", esso quando riceve un messaggio dall'esp32 stabilisce che tipo di messaggio sia, lo decompone grazie alle funzioni dichiarate in decompose.py e poi inserisce le informazioni ottenute nell'opportuna funzione da funzioni_logica_mqtt.py per aggiornare il database, oltre a cio`, rimanda anche indietro i messaggi per indicare all'esp32 a chi mandare cosa

## Installazione e primo avvio

#### Per prima cosa assicurarsi di aver installato python, pip e git, i seguenti comandi valgono dalla shell bash su una qualsiasi distro linux(testati ubuntu 22.04 LTS e debian 11), se non presenti nel sistema verranno installati:
```
sudo apt install python
sudo apt install python3-pip
sudo apt install git
```
#### Poi clonare questa repository in una cartella di posizione arbitraria:
```
git clone https://github.com/Tizio1234/rete_mqtt_nodi_lora.git
```
#### Eseguire il seguente comando dalla cartella radice del progetto per installare i moduli python necessari, se si creano dei conflitti di dipendenze, conviene usare un [ambiente virtuale python](https://docs.python.org/3.9/library/venv.html):
```
pip install -r requirements.txt
```
#### Entrare nella cartella gestione_schede_lora_1 ed eseguire i seguenti comandi per preparare il database Django:
```
python manage.py makemigrations
python manage.py migrate
```
#### Ora che il database e pronto dobbiamo solamente configurare la porta seriale a cui si colleghera l'esp32(ancora dobbiamo realizzare le librerie varie per l'esp32 master e i nodi)
...(da continuare)