from brain import generate_response,add_context,context_data,save_name_in_history,save_history
from agent_rules import rules
import json
from ui import welcome_message,goodbye_message
from commands import system_commands,execute_command
print(welcome_message())
print(system_commands)
while True:
    key=int(input("enter the command sir:"))
    if key==7:
        print(goodbye_message())
        break
    result=execute_command(key)
    
    
    
    if result[0]==16 or result[0]==17:
        if result[0]==16:
            add_context(rules)
        while True:
            user_asked=input("user:")
            
    
            if user_asked=="end":
                save_name_in_history(result[1])

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

    
#this main loop is to yet be checked especilaly the result[0]=17 parrt , i have defined lll the commmands , stil have to check the 
#history saving and loading funvctions 