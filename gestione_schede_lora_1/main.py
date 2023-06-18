# Setup database Django
from os import environ
environ.setdefault( "DJANGO_SETTINGS_MODULE", "gestione_schede_lora_1.settings")
import django
django.setup()
from funzioni_logica_mqtt import handle_pub_request, handle_sub_request, handle_unsub_request
from mqtt_lora.models import Scheda, Topic

# Import funzioni  da decompose per convertire i messaggi ricevuti dell'esp32 in oggetti
from decompose import decompose_pub_request, decompose_sub_request, decompose_unsub_request

from compose import compose_message

# Import funzione sleep per non sovraccaricare il sistema
from time import sleep

# Setup porta seriale
from serial import Serial, SerialException
esp32 = None

while True:
    try:
        esp32 = Serial("/dev/virtualport1", 115200)
        break
    except SerialException:
        sleep(1)

# Import libreria re per interpretare i messaggi ricevuti in seriale
import re

# Import file regex_formats dove ci sono i vari formati regex per interpretare i messaggi
import regex_formats

# Inizio programma vero e proprio
while True:
    sleep(.1)
    # Leggi intero buffer seriale nella variabile data
    data = esp32.read_all()

    # Se data e` vuoto allora rinizia
    if not data: continue

    print("Data received: ", data, sep=None)

    # Interpreta messaggio secondo il formato generale di un messaggio
    message_match = re.match(regex_formats.general_message_format, data, flags=re.DOTALL)

    # Se non c'e` stato alcun match riinizia da capo
    if message_match is None: continue

    message_type, message_content = message_match.groups()

    if message_type == b"S":
        scheda, topic = decompose_sub_request(message_content)
        handle_sub_request(scheda, topic)
        print("handled sub request")
    elif message_type == b"U":
        scheda, topic = decompose_unsub_request(message_content)
        handle_unsub_request(scheda, topic)
        print("handled unsub request")
    elif message_type == b"P":
        topic, message = decompose_pub_request(message_content)
        schede = handle_pub_request(topic, message)
        if schede is not None:
            for scheda in schede:
                output = compose_message(scheda, message, topic)
                esp32.write(output)
                #print(output)
                sleep(2)
        print("handled pub request")
