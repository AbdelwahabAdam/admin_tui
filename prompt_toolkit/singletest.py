from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
session = PromptSession(history=FileHistory('./myhistory'))
while True:
    session.prompt()