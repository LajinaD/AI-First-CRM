from app.database import SessionLocal
from agent.tools import edit_interaction_tool

db = SessionLocal()

result = edit_interaction_tool(
    db,
    "Change the sentiment of Dr Rahul Sharma to Neutral."
)

print(result)

db.close()