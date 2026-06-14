from brain import generate_response,add_context,context_data
from agent_rules import rules
add_context(rules)
while True:
    user_asked=input("ask something:")
    user_context={"role":"user","content":user_asked}
    add_context(user_context)
    
    if user_asked=="1":
            break
    try:
        print("agent thinking...")
        messages=context_data()
        response=generate_response(messages)       
        print(response)
        response_context={"role":"assistant","content":response}
        add_context(response_context)
    except Exception as e:
        print("error in this loop:",e)
