from openai import OpenAI
from databaseFlirt import intoDatabase


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


putEmbeddingIntoDB("Hello table!")




    
    

# If you still want to apply it to a DataFrame and see the result without exporting:
# import pandas as pd
# df = pd.DataFrame({'combined': ["Hello, how are you?", "Goodbye now!"]})
# df['ada_embedding'] = df.combined.apply(get_embedding)
# print(df)

# model: text-embedding-3-small
