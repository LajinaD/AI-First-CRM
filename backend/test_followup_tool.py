from app.database import SessionLocal
from agent.tools import follow_up_tool

db = SessionLocal()

result = follow_up_tool(db)

print(result)

db.close()