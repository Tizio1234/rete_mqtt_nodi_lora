from mqtt_lora.models import Scheda, Topic

def compose_message(scheda:Scheda, message:str, topic:Topic):
    buffer = bytearray()
    buffer += b"M"
    buffer += scheda.add_h.to_bytes(1, "big")
    buffer += scheda.add_l.to_bytes(1, "big")
    buffer += scheda.chan.to_bytes(1, "big")
    buffer += topic.nome.encode("utf-8")
    buffer += b"\r"
    buffer += message.encode("utf-8")
    buffer += b"\n"
    buffer += b"\x21"
    return buffer
