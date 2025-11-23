# question_sets.py
# Clean role-specific question bank.

class QuestionBank:
    def __init__(self):
        self.pointers = {}

        self.questions = {
            "software_engineer": [
                "Tell me about a challenging bug you solved recently.",
                "Explain a technical project you are proud of.",
                "Describe how you would design a login system."
            ],
            "sales": [
                "How do you handle objections from customers?",
                "Give an example where you turned a hesitant lead into a customer.",
                "How would you explain a product to someone uninterested?"
            ],
            "retail_associate": [
                "How do you deal with frustrated customers?",
                "Describe a time you improved store workflow.",
                "What would you do if the inventory didn’t match?"
            ]
        }

    def get_next(self, role, session_id):
        role = role if role in self.questions else "retail_associate"
        pointer = self.pointers.get(session_id, 0)
        q = self.questions[role][pointer % len(self.questions[role])]
        self.pointers[session_id] = pointer + 1
        return q


QUESTION_BANK = QuestionBank()
