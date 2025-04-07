from pydantic import BaseModel
from enum import Enum


class Message(BaseModel):

    content: str
    fromAi: bool