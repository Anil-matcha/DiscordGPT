# bot.py
import os
import discord
from reader import WebpageQATool
from langchain.chat_models import ChatOpenAI
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
TOKEN = "OTcwOTMzODc4MDgyNjY2NTE2.GSCSzd.Zr_UVei-ZxnzaxKRJe-oy-h0ms8DbwN9dLEW40"
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        llm = ChatOpenAI(temperature=1.0)
        query_website_tool = WebpageQATool(qa_chain=load_qa_with_sources_chain(llm))
        url = "https://uuki.live/"
        output = query_website_tool.run(message.clean_content+","+url)["output_text"]
        await message.reply(output)

client.run(TOKEN)