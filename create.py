import os
import json
import random

# Ask for user input
title = input("Enter the title: ")
description = input("Enter the description: ")

# Create the archive folder if it doesn't exist
if not os.path.exists("archive"):
    os.mkdir("archive")

# Generate a random 4-digit number
folder_name = str(random.randint(0, 9999)).zfill(4)

# Check if the folder already exists, regenerate the number if it does
while os.path.exists(os.path.join("archive", folder_name)):
    folder_name = str(random.randint(0, 9999)).zfill(4)

# Create the folder
folder_path = os.path.join("archive", folder_name)
os.mkdir(folder_path)

# Create the message.json file
message_data = {
    "title": title,
    "description": description
}
message_file_path = os.path.join(folder_path, "message.json")
with open(message_file_path, "w", encoding="utf-8") as file:
    json.dump(message_data, file, indent=4, ensure_ascii=False)

print(f"A new folder '{folder_name}' was created in 'archive' with the message.json file.")
