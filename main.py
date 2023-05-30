import discord
import os
import json
from discord.ext import commands
from subprocess import Popen

# Read the config file
with open('config.json') as config_file:
    config = json.load(config_file)

# Get the values from the config
token = config['token']
prefix = config['prefix']
webserver = config['webserver']
archive_path = config['archive-path']

# Initialize the Discord Bot object
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user.name}')
    # Start the webserver
    print(os.getcwd())
    try:
        Popen(["python3", "webserver.py"])
    except:
        Popen(["python", "webserver.py"])

    for guild in bot.guilds:
        print(guild.name)

@bot.event
async def on_message(message):
    if message.author == bot.user:  # Ignore messages from the bot itself
        return

    if isinstance(message.channel, discord.DMChannel):  # Only react to DMs
        content = message.content
        if content.isdigit() and len(content) == 4:
            code = content

            # Check if the code folder exists
            folder_path = os.path.join(archive_path, code)
            if os.path.isdir(folder_path):
                # Find the zip file inside the code folder
                zip_file = None
                for file in os.listdir(folder_path):
                    if file.endswith('.zip'):
                        zip_file = file
                        break

                # Check if a zip file was found
                if zip_file:
                    # Read the contents of the JSON message file
                    message_file = os.path.join(folder_path, 'message.json')
                    if os.path.isfile(message_file):
                        with open(message_file, 'r', encoding='utf-8') as file:
                            json_data = json.load(file)
                        title = json_data.get('title')
                        description = json_data.get('description')

                        # Check if a thumbnail file exists
                        thumbnail_path = os.path.join(folder_path, 'thumbnail.png')
                        thumbnail_exists = os.path.isfile(thumbnail_path)
                        if os.path.isfile(thumbnail_path):
                            # Create a Rich Embed with the thumbnail
                            embed = discord.Embed(title=title, color=discord.Color.green())
                            embed.set_image(url=f'attachment://{os.path.basename(thumbnail_path)}')
                        else:
                            # Create a Rich Embed without a thumbnail
                            embed = discord.Embed(title=title, color=discord.Color.green())

                        # Create the response text with the download link
                        download_link = f"[Click Here](https://{webserver}/downloads/{code}/{zip_file})"
                        embed.add_field(name="Download", value=download_link, inline=False)
                        embed.add_field(name="Description", value=description, inline=False)

                        # Send the embed with the thumbnail
                        if thumbnail_exists:
                            await message.channel.send(embed=embed, file=discord.File(thumbnail_path, filename='thumbnail.png'))
                        else:
                            await message.channel.send(embed=embed)
                    else:
                        await message.channel.send(f"Download link: {download_link}\nNo message found.")
                else:
                    await message.channel.send(f"No zip file found for the code {code}.")
            else:
                await message.channel.send(f"No folder found for the code {code}.")
        else:
            await message.channel.send("Invalid code. Please enter a 4-digit numerical code.")

    await bot.process_commands(message)


bot.run(token)
