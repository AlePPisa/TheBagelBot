import discord
from Scrapper import search, search_reddit
# Work with Python 3.6
import random
import os
from dotenv import load_dotenv
from Embedding import embedding

# Attributes
russian_players = {}
load_dotenv()
BOT_TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()


# Main Functions
@client.event
async def on_ready():
    print(f"{client.user} has joined the server!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("-nudes"):
        await search_google(message)

    if message.content.startswith("?nudes"):
        await message.channel.send(embed=embedding("-nudes: ","This command will look online and return \"nudes\" on "
                                                             "the given input\n-nudes [input]","White"))

    if message.content.startswith("-reddit"):
        await reddit(message)

    if message.content.startswith("?reddit"):
        await message.channel.send(embed=embedding("-reddit: ","This command will look online and hopefully return a meme of the given "
                                   "input\n-reddit [input]","White"))

    if message.content.startswith("-8ball"):
        await eight_ball(message)

    if message.content.startswith("?8ball"):
        await message.channel.send(embed=embedding("-8Ball: ","Using the newest, and most improved AI, this command will let you know how likely "
                                   "it is for a given situation to happen\n-8ball [situation]","White"))

    if message.content.startswith("-ready up"):
        await russian_setup(message)

    if message.content.startswith("?ready up"):
        await message.channel.send(embed=embedding("-ready up: ","This command adds you to the russian roulette game!","White"))

    if message.content.startswith("-shoot"):
        if len(russian_players) == 0:
            await message.channel.send(embed=embedding("Hold Up!", "You have to call -> {-ready up} before shooting.", "Red"))
        await shoot(message)

    if message.content.startswith("?shoot"):
        await message.channel.send(embed=embedding("-shoot", "This command shoots the loaded revolver into your skull!", "White"))

    if message.content.startswith("-restart"):
        await restart(message)

    if message.content.startswith("?restart"):
        await message.channel.send(embed=embedding("-restart: ","This command resets the current game of russian roulette, everyone needs to ready "
                                   "up again","White"))

    if message.content.startswith("!h") or message.content.startswith("!help"):
        await message.channel.send("The following commands exist: \n-nudes [search]\n-reddit [search]\n-8ball ["
                                   "situation]\n-ready up \n-shoot \n-restart\nFor any additional information on a "
                                   "specific command, type the command with a question mark instead of a dash e.x. "
                                   "\"?8ball\"")


# Functionality Functions
async def eight_ball(message):
    channel = message.channel
    with open("./8Ball") as f:
        possible_responses = f.read().split("\n")
    await channel.send(embed=embedding(random.choice(possible_responses) + ", " + message.author.mention,"Blue"))


async def reddit(message):
    channel = message.channel
    try:
        _, *search_item = message.content.split(" ")
        search_item = " ".join(search_item)
        res = search_reddit(search_item)
        print(res)
        await channel.send(res)
    except IndexError as e:
        print(e)
        await channel.send("Incorrect Syntax, try: -reddit [search]")
    except Exception as e:
        print(e)
        await channel.send("Can only request one at a time", e)


async def search_google(message):
    channel = message.channel
    try:
        _, *search_item = message.content.split(" ")
        search_item = " ".join(search_item)
        res = search("nudes " + search_item)
        print(res)
        await channel.send(res)
    except IndexError as e:
        print(e)
        await channel.send("Incorrect Syntax, try: -nudes [search]")
    except Exception as e:
        print(e)
        await channel.send("Can only request one at a time")


async def russian_setup(msg):
    if msg.author.name not in russian_players:
        russian_players[msg.author.name] = True
        await msg.channel.send(
            msg.author.mention + " is ready.\n" + "Current Players:\n" + "\n".join(list(p for p in russian_players)))
    else:
        await msg.channel.send(msg.author.mention + " you are already ready.")


async def restart(msg):
    global russian_players
    await msg.channel.send("Game has been restarted")
    russian_players = {}


async def shoot(msg):
    if russian_players[msg.author.name] == True:
        if random.randint(1, 7) == 6:
            russian_players[msg.author.name] = False
            await msg.channel.send(msg.author.mention + " is dead")
        else:
            await msg.channel.send(msg.author.mention + " is still alive")


@client.event
async def on_read():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("-----")


client.run(BOT_TOKEN)
