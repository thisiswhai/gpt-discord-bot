from dataclasses import dataclass
from typing import Optional, List

# SEPARATOR_TOKEN = "<|endoftext|>"


@dataclass(frozen=True)
class Message:
    role: str
    content: str

    def render(self):
        return {'role': self.role, 'content': self.content}


@dataclass
class Conversation:
    messages: List[Message]

    def prepend(self, message: Message):
        self.messages.insert(0, message)
        return self

    def render(self):
        return [message.render() for message in self.messages]


@dataclass(frozen=True)
class Config:
    name: str
    instructions: str
    # example_conversations: List[Conversation]


@dataclass(frozen=True)
class Prompt:
    header: Message
    # examples: List[Conversation]
    convo: Conversation

    def render(self):
        full_convo = self.convo.prepend(self.header)
        return full_convo.render()
