import discord
from discord.ext import commands
from utils import *
import openai as ai
from IPython.display import Image

Bot = commands.Bot(command_prefix= "!", intents= discord.Intents.all())

@Bot.event
async def on_ready():  # on_ready program ilk başlatıldığında çalışır.
    print("Hazırım! ")


@Bot.command()
async def sor(ctx, *, soru):

    ai.api_key = "Chat GPT TOKEN"
    ai_model = "gpt-3.5-turbo"

    cevap = ai.ChatCompletion.create(
        model=ai_model,
        messages=[{"role": "user", "content": soru}]
    )

    await ctx.send(cevap["choices"][0]["message"]["content"].strip())


@Bot.command()
async def çiz(ctx, *, soru):
    ai.api_key = "Chat GPT TOKEN"
    ai_model = "gpt-3.5-turbo"

    cevap = ai.Image.create(
        prompt=soru,
        n=1,
        size="512x512"
    )

    resim_url = cevap['data'][0]['url']


    Image(url=resim_url, width=512, height=512)

    await ctx.send(resim_url)


Bot.run("Discord Bot TOKEN")
