from openai import OpenAI
from database import intoDatabase


# Securely getting your API key
api_key = "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"
client = OpenAI(api_key=api_key)

def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    response = client.embeddings.create(input=[text], model=model)
    return response.data[0].embedding

# Example usage

    
    
def putEmbeddingIntoDB(text):
    
    vector=get_embedding(text)
    vector_str = ','.join(map(str, vector))
    
    intoDatabase(1,text,vector_str)


putEmbeddingIntoDB("I like sharks!")
putEmbeddingIntoDB("Sharks are cute animals!")
putEmbeddingIntoDB("Chicken tastes good")
putEmbeddingIntoDB("Dogs are adorable pets!!")
putEmbeddingIntoDB("The industrial revolution has been a disaster for the human race")
putEmbeddingIntoDB("Baby shark doo dooo doo")
putEmbeddingIntoDB("China is a powerful technology nation")
putEmbeddingIntoDB("Gayness is completely valid! IT's OKAY TO LIKE CUTE TWINKS!!")
putEmbeddingIntoDB("Homoseuality is a disease")
putEmbeddingIntoDB("I wonder what the future innovations in tech be like..hmm")








    
    

# If you still want to apply it to a DataFrame and see the result without exporting:
# import pandas as pd
# df = pd.DataFrame({'combined': ["Hello, how are you?", "Goodbye now!"]})
# df['ada_embedding'] = df.combined.apply(get_embedding)
# print(df)

# model: text-embedding-3-small
