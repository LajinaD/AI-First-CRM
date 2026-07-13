from agent.graph import graph

messages = [

    "I met Dr Rahul Sharma today and discussed Ozempic.",

    "Change the sentiment of Dr Rahul Sharma to Neutral.",

    "Find Dr Rahul Sharma",

    "Show interaction history of Dr Rahul Sharma",

    "Who needs follow up?",

    "Hello"

]

for message in messages:

    result = graph.invoke({

        "message": message,

        "intent": "",

        "response": "",

        "tool_result": {}

    })

    print("=" * 60)
    print(message)
    print(result["intent"])
    print(result["response"])