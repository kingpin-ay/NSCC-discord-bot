import os
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv
from questionGen import gen 


load_dotenv()
TOKEN = os.getenv('TOKEN')




intents = discord.Intents.all()
bot = commands.Bot(command_prefix='=' , intents= intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')




@bot.command()
async def hello(ctx):
    await ctx.send(f"hello")


@bot.command()
async def quizc(ctx):
    q = gen()
    for i in range(0,len(q)):
        qst = q[i].ques()
        qst += "\n" + q[i].opt() + "\nYou have 15sec to reply to this question."
        message = await ctx.send(qst)
        time.sleep(10)
        await ctx.send(f"The correct answer for the previous quesion is : {q[i].answer}")
        await message.delete()


        


# Run the bot
bot.run(TOKEN)
