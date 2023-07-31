# import openai 
from key import CHAGPT_API
import requests as rg


def gerar_resposta(mensagem):
  

    link = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {CHAGPT_API}", "Content-Type": "application/json"
    }
    body = {
        "model": "gpt-3.5-turbo", 
        "messages": mensagem
    }
    # body_josn = json.dumps(body)

    requisisão = rg.post(link, headers= headers,json= body)
    resposta = requisisão.json()
    return resposta["choices"][0]["message"]["content"]


