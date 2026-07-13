from agent.graph import graph

result = graph.invoke(
    {
        "message": "I met Dr Rahul Sharma today and discussed Ozempic.",
        "intent": "",
        "response": "",
    }
)

print(result)