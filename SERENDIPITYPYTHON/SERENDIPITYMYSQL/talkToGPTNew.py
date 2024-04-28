from openai import OpenAI
import tiktoken
from embedding import putEmbeddingIntoDB
from database import clearDatabase



customInstruction=""

client = OpenAI(
    api_key='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'
)

def chat_with_gpt(text, chat_log=None, time=1):
    
    chat_log = []


    
    chat_log.append({"role": "user", "content": text}) #NEED TO CHANGE THIS  'text'

    # Generate the completion
    chat_completion = client.chat.completions.create(
        messages=chat_log,
        model="gpt-3.5-turbo"
    )

    # Append the model's response to the conversation history
    response = chat_completion.choices[0].message.content
    

    AIResponse= "(Time: "+ str(time) + "). " + response
    putEmbeddingIntoDB(AIResponse)
    
    AIResponseNew = "AI: "+ "(Time: "+ str(time) + "). " + response
    
    print(AIResponseNew)
    
    
    
    return chat_log, AIResponse

def run_chat():
    text = "hi!!"
    chat_log = None
    time=1 #Hopefully chatGPT is smart enough to figure out whatt to do with this UwU
    
    olderMsg=""
    oldMsg=""
    
    
    while text != "end":
        
        olderMsg=oldMsg
        text+= customInstruction
        chat_log, oldMsg = chat_with_gpt(text, chat_log, time)
        text = input("You: ")
        time+=1 
    
    print("TY TH END!")
    clearDatabase()

run_chat()
