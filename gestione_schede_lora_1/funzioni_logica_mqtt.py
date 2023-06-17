from mqtt_lora.models import Scheda, Topic, DataBaseMessage

def handle_sub_request(scheda: Scheda, topic: Topic) -> None:
    database_topic = Topic.objects.get_or_create(nome=topic.nome)[0]
    database_scheda = Scheda.objects.get_or_create(add_h=scheda.add_h, add_l=scheda.add_l, chan=scheda.chan)[0]

    database_topic.schede.add(database_scheda)

def handle_pub_request(topic:Topic, message:str) -> Scheda:
    database_topic = Topic.objects.get_or_create(nome=topic.nome)[0]
    DataBaseMessage.objects.create(topic=database_topic, message_content=message)

    return database_topic.schede.all()

def handle_unsub_request(scheda:Scheda, topic:Topic) -> None:
    try:
        database_scheda = Scheda.objects.get(add_h=scheda.add_h, add_l=scheda.add_l, chan=scheda.chan)
        database_topic = Topic.objects.get(nome=topic.nome)
    except (Scheda.DoesNotExist, Topic.DoesNotExist):
        return

    database_topic.schede.remove(database_scheda)
