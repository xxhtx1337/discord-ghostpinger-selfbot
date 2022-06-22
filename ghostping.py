from discord.ext import commands
from random import randint
import time
from time import sleep

client = commands.Bot(
  command_prefix='-',
  self_bot=True,
  help_command=None
)

@client.event
async def on_message(message):
  if message.author == client.user: # Skips if it's the account message
    return

  if len(message.content) > 0: # Proceeds to ghostping anyone sending a message
    sleep(randint(1,5)) # Random delay in seconds from 1 to 5 secs
    await message.channel.send("<@"+str(message.author.id)+">", delete_after=0) # Ghostpings the user
    print("-------------------------------------------------------")
    print("ID: "+str(message.author.id)+" | Name in Server: "+message.author.display_name+"\n"+message.author.name+"#"+message.author.discriminator+" was pinged on "+time.strftime('%d/%m/%Y at %H:%M:%S'))
    print("-------------------------------------------------------")

client.run("token-here", bot=False)
