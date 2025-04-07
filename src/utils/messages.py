
import queue

from src.schema.message import Message

message_store = dict()

def get_messages(session_id: str):

    if session_id not in message_store:
        message_store[session_id] = queue.Queue(maxsize=100)

    return list(message_store[session_id].queue)

def add_message(session_id: str, message: Message):
    if session_id not in message_store:
        message_store[session_id] = queue.Queue(maxsize=100)

    if message_store[session_id].full():
        message_store[session_id].get()

    message_store[session_id].put(message)