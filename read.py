import os
import json

# Read the config file
with open('config.json') as config_file:
    config = json.load(config_file)

# Get the archive path from the config
archive_folder_path = config['archive-path']

# Get a list of all subdirectories (4-digit code folders) in the archive folder
subdirectories = [name for name in os.listdir(archive_folder_path) if os.path.isdir(os.path.join(archive_folder_path, name))]

# Create a dictionary to store the folder code as key and title as value
folder_titles = {}

# Iterate through each subdirectory
for subdirectory in subdirectories:
    folder_path = os.path.join(archive_folder_path, subdirectory)
    json_file_path = os.path.join(folder_path, 'message.json')

    # Check if the json file exists in the current folder
    if os.path.isfile(json_file_path):
        with open(json_file_path, 'r') as json_file:
            try:
                data = json.load(json_file)
                title = data.get('title')
                folder_titles[subdirectory] = title
            except json.JSONDecodeError:
                # Handle invalid JSON file if needed
                pass
    else:
        # If message.json doesn't exist, leave the title empty
        folder_titles[subdirectory] = ""

# Sort the folder titles by their names
sorted_folder_titles = {k: v for k, v in sorted(folder_titles.items(), key=lambda item: item[1])}

# Create a new JSON file to store the sorted folder titles
output_file_path = './database.json'

# Check if the output file already exists
if not os.path.isfile(output_file_path):
    # Create an empty dictionary to store the folder titles
    empty_titles = {}

    # Write the empty dictionary to the output file
    with open(output_file_path, 'w') as output_file:
        json.dump(empty_titles, output_file)

    print("Created empty database file:", output_file_path)

# Open the output file for writing the sorted folder titles
with open(output_file_path, 'w') as output_file:
    json.dump(sorted_folder_titles, output_file, indent=4)

print("Folder titles extracted and saved to", output_file_path)
