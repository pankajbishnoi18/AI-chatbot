from litellm import completion
from commands import execute_command
import json
def generate_response(messages):
    response=completion(
        model="ollama/llama3",
        messages=messages,
        base_url="http://localhost:11434",
        temperature=0.1
)

    return response.choices[0].message.content

def context_data():
    with open("context.json","r")as file:
        data=json.load(file)
    return data

  
def add_context(context):
    data=context_data()
    
    data.append(context)
    with open("context.json","w")as file:
        json.dump(data,file,indent=3)
    
def save_history(key,result):
    context_data=context_data()
    old_history=show_history()
    new_data={
        "user commanded":key,
        "bot responded0":result
    }
    old_history.append(new_data)  
    with open("history.json","w")as file:
        json.dump(old_history,file)
def show_history():
    with open("history.json","r")as file:
        old_history=json.load(file)
    
    return old_history
def save_name_in_history(name):
    chat={name:[]}
    old_history=show_chat_history()
    old_history.append(chat)
    return old_history,name



