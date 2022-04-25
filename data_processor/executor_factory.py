from .message_executors import random_num_gen_executor
from enum import Topics


def get_message_executor(topic_name):
    if topic_name == Topics.random_num_gen:
        return random_num_gen_executor.message_executor
    else:
        raise Exception("Topic %s not found" % topic_name)
