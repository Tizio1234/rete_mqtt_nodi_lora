from mqtt_lora.models import Scheda, Topic
from regex_formats import pub_request_format, sub_request_format, unsub_request_format
import re

def decompose_sub_request(message:bytearray) -> tuple[Scheda, Topic]:
    """
    Given a sub/unsub request from the esp32 it returns the necessary objects to store in the database
    """
    board_information, topic_name = re.match(sub_request_format, message, flags=re.DOTALL).groups()
    return (Scheda(add_h=board_information[0], add_l=board_information[1], chan=board_information[2]), Topic(nome=topic_name.decode("utf-8")))

def decompose_pub_request(message:bytearray) -> tuple[Topic, str]:
    """
    Given a pub request sent from the esp32 it returns the necessary objects to store in the database
    """
    topic_name, message_content = re.match(pub_request_format, message, flags=re.DOTALL).groups()
    return (Topic(nome=topic_name.decode("utf-8")), message_content.decode("utf-8"))

decompose_unsub_request = decompose_sub_request
