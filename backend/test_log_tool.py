from app.database import SessionLocal
from agent.tools import log_interaction_tool

db = SessionLocal()

result = log_interaction_tool(
    db,
    """
    I met Dr Rahul Sharma today at 11 AM.

    We discussed Ozempic.

    Doctor was positive.

    Follow up after two weeks.
    """
)

print(result)

db.close()