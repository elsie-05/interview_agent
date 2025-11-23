# memory_store.py
# Stores questions/answers per session.

class MemoryStore:
    def __init__(self):
        self.data = {}

    def store_question(self, session_id, q):
        self.data.setdefault(session_id, {"questions": [], "answers": []})
        self.data[session_id]["questions"].append(q)

    def store_answer(self, session_id, a):
        self.data.setdefault(session_id, {"questions": [], "answers": []})
        self.data[session_id]["answers"].append(a)

    def get_all_answers(self, session_id):
        return self.data.get(session_id, {}).get("answers", [])
