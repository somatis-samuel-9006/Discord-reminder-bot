import discord
import random
import os
from discord.ext import commands, tasks
from keep_alive import keep_alive


#use ! for bot
bot = commands.Bot("!")
#target chat id
#channel_id = <insert chat id here>

#the bot token
my_secret = os.environ['TOKEN']


@bot.event
async def on_message(message):
  if bot.user.mentioned_in(message):
    await message.channel.send("Hello! Commands:\n!joke: Tell a water-based joke\n!tutorial: Teach you how to drink water")
  await bot.process_commands(message)

#open jokes file and read in content to list
f = open("jokes.txt", "r")
jokes = f.readlines()

#joke command, THE NAME OF THE FUNCTION == THE NAME OF THE COMMAND
@bot.command()
async def joke(ctx):
  #use random.choice to get a random element from the jokes list
  await ctx.send(random.choice(jokes))

#water tutorial
@bot.command()
async def tutorial(ctx):
  await ctx.send("https://www.youtube.com/watch?v=STH4_cETyFk&ab_channel=HamzaAhmed")

#use tasks loop to send a water reminder every x seconds
#1800 seconds in a half hour
@tasks.loop(seconds=1800)
async def drink_water():
    message_channel = bot.get_channel(channel_id)
    #role id of role to ping for reminder
    await message_channel.send("<@&insertroleidhere> It's time to drink some water!")

@drink_water.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

keep_alive()
drink_water.start()
bot.run(my_secret)
