

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

from .dialogue_manager import DialogueManager
from .feedback_engine import FeedbackEngine
from .memory_store import MemoryStore
from .question_sets import QUESTION_BANK

app = FastAPI(title="Interview Practice Partner")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
session_memory = MemoryStore()
dialogue_manager = DialogueManager(QUESTION_BANK, session_memory)
feedback_engine = FeedbackEngine()


class UserTurn(BaseModel):
    session_id: str
    role: str
    user_message: Optional[str] = None
    request_next: bool = False
    end_interview: bool = False


@app.post("/interview")
def handle_interview_turn(turn: UserTurn):
    """
    Main conversational API.
    Returns: next question, follow-up, repair message, or final report.
    """

    
    if turn.request_next and not turn.user_message:
        q = dialogue_manager.get_next_question(turn.session_id, turn.role)
        return {"type": "question", "message": q}

    
    if turn.user_message and not turn.end_interview:
        outcome = dialogue_manager.process_answer(turn.session_id, turn.user_message)

        
        if outcome["action"] == "followup":
            return {"type": "followup", "message": outcome["message"]}

        
        if outcome["action"] == "invalid":
            return {"type": "repair", "message": outcome["message"]}

        
        next_q = dialogue_manager.get_next_question(turn.session_id, turn.role)
        return {
            "type": "acknowledge",
            "message": "Thanks, noted. Here is the next question:",
            "next_question": next_q
        }

    
    if turn.end_interview:
        answers = session_memory.get_all_answers(turn.session_id)
        report = feedback_engine.generate_report(answers, turn.role)
        return {"type": "report", "report": report}

    return {"type": "info", "message": "Send a message or request_next=true."}
