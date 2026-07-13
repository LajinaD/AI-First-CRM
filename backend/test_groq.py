from services.groq_service import llm

response = llm.invoke("Say hello in one sentence.")

print(response.content)