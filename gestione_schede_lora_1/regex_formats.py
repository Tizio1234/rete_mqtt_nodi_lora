general_message_format = rb"^(?P<message_type>[PUS])(?P<message_content>[^\n]+).\n$"

pub_request_format = rb"^(?P<topic_name>[^\r]+)\r(?P<message_content>.+)$"

sub_request_format = rb"^(?P<board_informations>.{3})(?P<topic_name>.+)$"

unsub_request_format = sub_request_format