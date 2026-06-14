import json
from brain import show_history
system_commands={
    
    2:"to start a new chat",
    "end":"to end the conversation",
    3:"to show all chats",
    4:"to continue a chat from existing chat",
    
    6:"to view the commands log",
    7:"to shut down the bot"
}
def execute_command(key):
    if key not in system_commands:
        return "invalid command"
    if key==2:
        with open("context.json","w")as file:
            json.dump([],file)
        name_of_chat=input("enter the name of this chat:")
        return 16,name_of_chat
    if key==6:
        return system_commands
    if key==3:
        all_chats=[]
        history=show_history()
        for i in history:
            if len(i)==1:
                all_chats.append(list(i.keys())[0])
        return all_chats
    if key==4:
        all_chats=execute_command(3)
        chat=input("enter the name of the chat you want me to open:")
        if chat in all_chats:
            history=show_history()
            for i in history:
                if len(i)==1 and list(i.keys())[0]==chat:
                    data=list(i.values())[0]
                    with open("context.json","w") as file:
                        json.dump(data,file)
                    
        return 17



