import mysql.connector
import tiktoken


from embedding  import get_embedding
mydb = mysql.connector.connect(
    host= "localhost",
    user="root",
    passwd="Bro123@bruh",
    database="serendipity"
)


myCursor = mydb.cursor()
myCursor.execute("SELECT * FROM memory")



maxTokens=3900 #since 60 is the boilerplate code.




#returns the text you must give to the LLM 
def finalUserText(msg1, msg2, userMsg):
    
    tokensAtDisposal = maxTokens #the amo
    
    boilerplateToken=60 #tokens for the boilerplate custom instruction
    recentMsgToken= tokenLength(msg1) + tokenLength(msg2) +3 #adding the numbrs is to account for the ' ' s
    userMsgToken= tokenLength(userMsg)+2
    tokensAtDisposal -=(boilerplateToken+recentMsgToken+userMsgToken)
    
    numList, textList = contextList(get_embedding(userMsg)) 
    
    
    total_tokens = 0
    result = []
    
    for text in textList:
        current_tokens = tokenLength(text)
        if total_tokens + current_tokens +2> tokensAtDisposal: #the +2 again, for the ' ' s
            break
        result.append("'" + text + "'")
        total_tokens += current_tokens
    
    if len(result) == 0:
        formatted_string= "None so far."
    # Join the list into a string with comma separation
    formatted_string = ", ".join(result)

    return formatted_string
    
    
    
    


#gives a list of all the previous messages IN DESCENDING ORDER OF RELEVANCE HAHAHAHAHA!!!!! YESS!! 
def contextList(vector0):

    textList=[]
    numList=[]

    myResult= myCursor.fetchall()

    for row in myResult:
        
        ID, text, vector = row
        textList.append(text)
        listVector=toList(vector)
        similarity = cosineSimilarity(vector0, listVector)
        numList.append(similarity)
    
    # OK by this time, ALL THE GOD DAMN SHIT IN THE FUCKING DATABASE SHOULD BE INSIDE THE TEXTLIST! 
    return quicksort_descending_with_texts(numList, textList)
    #ALRIGT THIS SHUT BETTER WORK LMFAO IT WORKS OKAY COOL!


#tools
#tools for a buncha silly stuff
#tools
#tools


def tokenLength(text):
# Get the tokenizer encoding for GPT-3.5 Turbo
    tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")


# Encode the text and find out the number of tokens
    tokens = tokenizer.encode(text)

    return len(tokens)




def toList(vector):
    
    return [float(x) for x in vector.split(',')]




def cosineSimilarity(A, B):

    # Calculate dot product
    dot_product = sum(a*b for a, b in zip(A, B))

    # Calculate the magnitude of each vector
    magnitude_A = sum(a*a for a in A)**0.5
    magnitude_B = sum(b*b for b in B)**0.5

    # Compute cosine similarity
    return (dot_product / (magnitude_A * magnitude_B))
    


def quicksort_descending_with_texts(arr, texts):
    if len(arr) <= 1:
        return arr, texts
    else:
        pivot = arr[0]
        pivot_text = texts[0]
        less_than_pivot = [x for x, t in zip(arr[1:], texts[1:]) if x >= pivot]
        less_than_pivot_texts = [t for x, t in zip(arr[1:], texts[1:]) if x >= pivot]
        greater_than_pivot = [x for x, t in zip(arr[1:], texts[1:]) if x < pivot]
        greater_than_pivot_texts = [t for x, t in zip(arr[1:], texts[1:]) if x < pivot]
        
        sorted_less, sorted_less_texts = quicksort_descending_with_texts(less_than_pivot, less_than_pivot_texts)
        sorted_greater, sorted_greater_texts = quicksort_descending_with_texts(greater_than_pivot, greater_than_pivot_texts)
        
        return sorted_less + [pivot] + sorted_greater, sorted_less_texts + [pivot_text] + sorted_greater_texts 
    # returns the sorted numbers, THEN the texts UwU


finalUserText("1","1","1")

