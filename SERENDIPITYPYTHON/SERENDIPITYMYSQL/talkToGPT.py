from openai import OpenAI
import tiktoken


customInstruction=" Just add 'UwU' at the end of the conversation, okay?"

client = OpenAI(
    api_key='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'
)

def chat_with_gpt(text, chat_log=None):
    if chat_log is None:
        chat_log = []

    # Append the new user message to the conversation history
    chat_log.append({"role": "user", "content": text})

    # Generate the completion
    chat_completion = client.chat.completions.create(
        messages=chat_log,
        model="gpt-3.5-turbo"
    )

    # Append the model's response to the conversation history
    response = chat_completion.choices[0].message.content
    chat_log.append({"role": "system", "content": response})

    print("AI: ", response)
    return chat_log

def run_chat():
    text = "hi!!"
    chat_log = None
    while text != "end":
        
        text+= customInstruction

        chat_log = chat_with_gpt(text, chat_log)
        text = input("You: ")
    
    print("TY TH END!")
    print(chat_log)

run_chat()
