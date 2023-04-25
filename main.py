import re
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# set up OpenAI API
openai.api_key = os.environ.get('open_ai_api_key')


# define function to read document
def read_document(filepath):
    with open(filepath, "r", encoding="utf8", errors='ignore') as file:
        document = file.read()
    return document


# define function to answer user queries
def answer_query(document, query):
    # preprocess query
    query = query.lower()
    query = re.sub(r'[^\w\s]', '', query)
    query = re.sub(r'\d+', '', query)
    # generate response from ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-003",  # List of models: https://platform.openai.com/docs/models
        prompt=document + "\nQuery: " + query + "\nAnswer:",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # extract answer from response
    answer = response.choices[0].text.strip()
    # return answer
    return answer


# example usage
filepath = "jokes.txt"  # place file in same directory as main.py
document = read_document(filepath)

query = "Summarize this document"  # Your prompt for what you want to do with the file
answer = answer_query(document, query)
print(answer)
