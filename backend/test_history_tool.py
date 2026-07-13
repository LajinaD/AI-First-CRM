from app.database import SessionLocal
from agent.tools import interaction_history_tool

db = SessionLocal()

result = interaction_history_tool(
    db,
    "Rahul"
)

print(result)

db.close()