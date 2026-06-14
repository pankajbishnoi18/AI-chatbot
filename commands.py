import json
from ui import goodbye_message


system_commands={
    
    2:"to start a new chat",
    "end":"to end the conversation",
    3:"to show all chats",
    4:"to resume existing chat",
    
    6:"to view the commands log",
    7:"to shut down the bot"
}
def show_history():
    with open("history.json","r")as file:
        old_history=json.load(file)    
    return old_history
def settle_the_duplicate_chat(i,chat):
    history=show_history()
                    
    new={"this chat has been resumed again by user somewhere ":"you willl find this chat where it was resumed"}
    history[history.index(i)] = new
    with open("history.json","w")as file:
        json.dump(history,file,indent=2)
def execute_command(key):
    if key not in system_commands:
        return "invalid command"
    if key==2:
        with open("context.json","w")as file:
            json.dump([],file)
        while True:
            name_of_chat=input("enter the name of this chat:")
            if name_of_chat in execute_command(3):
                print( f"{name_of_chat} already exists, try changing the name of the chat")
            else:
                break
        return "started a new chat",name_of_chat
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
                
                if list(i.keys())[0]==chat:
                    data=list(i.values())[0]
                    with open("context.json","w") as file:
                        json.dump(data,file,indent=3)
                    settle_the_duplicate_chat(i,chat)

                    return "opened the excisting chat",chat
                
           
        else:
            return "no such chat found",chat           
        


    if key==7:
        return  goodbye_message()



