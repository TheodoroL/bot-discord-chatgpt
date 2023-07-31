import discord
from discord.ext import commands
from key import DISORD_API
from resposta import gerar_resposta



config = []
intents=discord.Intents.all()

client = commands.Bot(command_prefix="!",intents= intents)

@client.event
async def on_ready():
    print('-'* len(client.user.name))
    print(client.user.name)
    print('-'* len(client.user.name))



@client.command(name="ajuda")
async def ajuda(mensagem):
    await mensagem.message.channel.send("Uma mensagem foi enviada para você, verefica o seu privado")
    await mensagem.message.author.send('''```
você pediu uma solicição de ajuda para usar os comando do bot chatgpt, então vamos lá...
----------------------------------------------------------------------------------------
Os comandos que tem são o !help (para solocitar ajuda de comandos do bot), o !pergunta que você utiliza para tirar
duvidas pelo chatgpt e o !pv que a mesma coisa que o !pergunta, só que ele manda a  resposta no seu pv 
--------------------------------------------------------------------------------------------------------------------
                    Ultilização do Bot
!pergunta : basicamente você vai colocar o comando !pergunta e a sua pergunta, exemplo:
                !pergunta o que é uma um computador ? 
!pv : é a mesma coisa que o !pergunta, só que a diferença é que ele vai mandar a resposta no seu privado, exemplo:
                !pv o que é uma memória secundaria ? 

!ajuda : você solicita ajuda para usar os comandos
        

```''')


@client.command(name="pergunta")
async def pergunta(mensagem, *pergunta):
    global config
    valor = {"role": "user", "content": " ".join(pergunta)}
    config.append(valor)
    
    resposta = gerar_resposta(config)
    
    if  len(resposta) > 2000:
        for contador in range(0, len(resposta), 1000):
            pedaço = resposta[contador:contador+1000]
            await mensagem.message.channel.send(pedaço)
    else:
        await mensagem.message.channel.send(resposta)

    if len(config) > 40       :
        config.pop(0)
 


@client.command(name="pv")
async def pv (mensagem, *pergunta):
    global config
    valor = {"role": "user", "content": "".join(pergunta)}
    config.append(valor)
   
    resposta = gerar_resposta(config)

    if len(resposta) > 2000:

        for contador in range(0, len(resposta), 1000):
            pedaço = resposta[contador:contador+1000]
            await mensagem.message.channel.send(pedaço)
    else:
        await mensagem.message.author.send(resposta)
    
    if len(config) > 40:
        config.pop(0)
   

client.run(DISORD_API)  
