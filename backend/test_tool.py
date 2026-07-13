from agent.tools import extract_interaction

result = extract_interaction(

"""
I met Dr Rahul Sharma today at 11 AM.

We discussed Ozempic.

Doctor was positive.

Follow up after two weeks.
"""

)

print(result)