from litellm import completion
import json
def response(messages):
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
def add_context(que,response):
    data=context_data()
    new_data={
        "user_asked":que,
        "chatbot replied":response
    }
    data.append(new_data)
    with open("context.json","w")as file:
        json.dump(data,file,indent=3)
    
def save_history():
    context_data=context_data()
    with open("history.json","r")as file:
        old_history=json.load(file)
    old_history.append(context_data)
    
    with open("history.json","w")as file:
        json.dump(old_history,file)


