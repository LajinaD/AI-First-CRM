from app.database import SessionLocal
from agent.tools import search_hcp_tool

db = SessionLocal()

result = search_hcp_tool(
    db,
    "Rahul"
)

print(result)

db.close()