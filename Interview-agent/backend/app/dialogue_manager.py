

import re
from .memory_store import MemoryStore


class DialogueManager:
    def __init__(self, question_bank, memory_store: MemoryStore):
        self.bank = question_bank
        self.memory = memory_store

    def get_next_question(self, session_id, role):
        question = self.bank.get_next(role, session_id)
        self.memory.store_question(session_id, question)
        return question

    def process_answer(self, session_id, user_answer):

        cleaned = user_answer.strip().lower()
        word_count = len(cleaned.split())

        
        confused_patterns = ["i don't know", "idk", "not sure", "can you repeat"]
        if any(p in cleaned for p in confused_patterns):
            return {"action": "followup", "message": "No worries. Walk me through how you might think about it."}

       
        if word_count < 5:
            return {"action": "followup", "message": "Could you explain a bit more?"}

       
        if word_count > 40 and ("friend" in cleaned or "yesterday" in cleaned):
            return {"action": "followup", "message": "I appreciate the detail. Could you relate that more directly to the question?"}

      
        if re.search(r"(asdf|blah|random|test)", cleaned):
            return {"action": "invalid", "message": "That doesn't seem related. Try answering clearly."}

     
        self.memory.store_answer(session_id, user_answer)
        return {"action": "ok"}
