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
    
    old_history=show_history()
    new_data={
        "user commanded":key,
        "bot responded":result
    }
    old_history.append(new_data)  
    with open("history.json","w")as file:
        json.dump(old_history,file,indent=2)

def show_history():
    with open("history.json","r")as file:
        old_history=json.load(file)    
    return old_history

def chat_saver(name):
    chat={name:context_data()}
    old_history=show_history()
    old_history.append(chat)
    with open("history.json","w")as file:
        json.dump(old_history,file,indent=2)
    return "chat saved successfully"

