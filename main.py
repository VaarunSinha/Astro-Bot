# import discord
import os
import requests
import json
from discord.ext import commands

# API REQUEST TO PEOPLE IN SPACE
reqUrl = "http://api.open-notify.org/astros.json"



response = requests.get(reqUrl)

JSON = json.loads(response.text)

people = JSON["people"]
nasa_key = os.environ['NasaApiKey']



client = commands.Bot(command_prefix='$')
discordToken = os.environ['discordToken']

@client.event
async def on_ready():
  print(f"We have logged in as {client.user}")
  
@client.command()
async def hs(ctx, arg):
    Data = json.loads(requests.get(f"http://horoscope-api.herokuapp.com/horoscope/today/{arg}").text)

    await ctx.send("Hororscope: {}".format(Data["horoscope"].capitalize()))


@client.command()
async def helpme(ctx):
 await ctx.send("List of commands:\n1.$hs {star}: this command takes your star, and messages your horoscope.\n 2. $pis: This command messages which astronauts are there in space right now!.\n 3. $joke this messages a fun joke!")

@client.command()
async def pis(ctx):
   await ctx.send("People In Space Right Now!")
   for person in people:
     await ctx.send("Name: {}, Craft: {}".format(person["name"], person["craft"]))

@client.command()
async def apod(ctx):
  Data = requests.get("https://api.nasa.gov/planetary/apod?api_key=wqkArrYMgtFxQKiVDsElqrGVXEMho0RsAV4qz5qf").text

  JSON = json.loads(Data)
  await ctx.send("Title: {} \n \n Date: {} \n \n Explanation: {} \n \n Copyright: {}\n \n Image URL: {}".format(JSON["title"], JSON["date"], JSON["explanation"], JSON["copyright"],JSON["hdurl"] ))

client.run(discordToken)
