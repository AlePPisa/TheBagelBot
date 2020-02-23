import discord

colors = {"Red":0xC70039, "Blue":0x33B2FF, "Green":0x58C656, "Purple":0x8F43DF, "White":0xFFFFFF}

def embedding(msg, color):
    if color in colors:
        return discord.Embed(description=msg, color=colors[color])
    else:
        return discord.Embed(description=msg, color=colors["White"])

def embedding(title, msg, color):
    if color in colors:
        return discord.Embed(title=title, description=msg, color=colors[color])
    else:
        return discord.Embed(title=title, description=msg, color=colors["White"])
