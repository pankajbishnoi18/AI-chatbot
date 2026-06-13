from brain import response,context_data
from agent_rules import rules
while True:
    user_asked=input("ask something:")
    que=[{"role":"user","content":user_asked}]
    if user_asked=="1":
            break
    try:
       
        print("agent thinking...")
        result=response(rules+context_data()+que)
        print(result)
    except Exception as e:
        print("error in this loop:",e)
