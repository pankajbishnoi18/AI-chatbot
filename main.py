from brain import generate_response,add_context,context_data,chat_saver,save_history
from agent_rules import rules
import json
from ui import welcome_message
from commands import system_commands,execute_command
print(welcome_message())
save_history("new_session-------------------------------------------------------------------------",welcome_message())
print(system_commands)
while True:
    key=int(input("enter the command sir:"))
    result=execute_command(key)
    if key==7:  
        save_history(key,result)
        print(result)

        break    
    if isinstance(result, tuple):
       
        if result[0]=="started a new chat":
            add_context(rules)
            save_history(key,"started a new chat")

        while True:
            user_asked=input("user:")
            
    
            if user_asked=="end":
                print(chat_saver(result[1]))

                break
            try:
                user_context={"role":"user","content":user_asked}
                add_context(user_context)
                print("agent thinking...")
                messages=context_data()
                response=generate_response(messages)       
                print(response)
                response_context={"role":"assistant","content":response}
                add_context(response_context)
            except Exception as e:
                print("error in this loop:",e)
    else:
        save_history(key,result)
        print(result)

    
