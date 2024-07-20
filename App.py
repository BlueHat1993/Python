# import ollama
# import fastapi
# from fastapi import FastAPI
# app=FastAPI()
# @app.get("/chatmessage/")
# def generatemessage(passage:str): 
#     response =  ollama.chat(model='mistral', messages=[
#   {
#     'role': 'user',
#     'content': 'create a sentiment analysis with sentiment label , score,keywords and output it in json from the passage-'+passage+"'"
#   },
 
# ],
#  format='json'
# )
#     return{response}

# import ollama
# passage="God is dead.God remains dead and we have killed him.We are happy people."
# response =  ollama.chat(model='mistral', messages=[
#   {
#     'role': 'user',
#     'content': 'create a sentiment analysis with sentiment label , score,keywords and output it in json from the passage-'+passage+"'"
#   },
 
# ],
#  format='json'
# )
# print(response)
import ollama
import fastapi
from fastapi import FastAPI 
import json

app = FastAPI()

@app.get("/chatmessage/")
def generatemessage(text: str):
    response = ollama.chat(
        model='mistral',
        messages=[
            {
                'role': 'user',
                'content': """label all the primary key emotions and its sentiments as postive or negative sentiment with 
                corresponding scores in 
                order of emotion,sentiment score as 'sentiment_val' in negative or postive integer and emotion score as 'emo_val'  from
                the text after ''' and create a json"+"'''"""+text
            },
        ],
        format='json'
    )
    # content = response['message']['content']
    # return {"content": content}
    return { json.dumps(response)}



