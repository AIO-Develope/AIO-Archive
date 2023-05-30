import os
import json
import zipfile

# Read the config file
with open('config.json') as config_file:
    config = json.load(config_file)

# Get the archive path from the config
archive_folder_path = config['archive-path']

# Get a list of all subdirectories (4-digit code folders) in the archive folder
subdirectories = [name for name in os.listdir(archive_folder_path) if os.path.isdir(os.path.join(archive_folder_path, name))]

# Create a dictionary to store the folder code as key and title and size as values
folder_data = {}

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
                folder_data[subdirectory] = {'title': title}
            except json.JSONDecodeError:
                # Handle invalid JSON file if needed
                pass
    else:
        # If message.json doesn't exist, leave the title empty
        folder_data[subdirectory] = {'title': ""}

    # Search for ZIP files in the current folder
    zip_files = [file for file in os.listdir(folder_path) if file.endswith('.zip')]

    if zip_files:
        # If ZIP file(s) found, get the size of the first file and format it as "X.XX GB"
        zip_file_path = os.path.join(folder_path, zip_files[0])
        zip_file_size = os.path.getsize(zip_file_path) / (1024 * 1024 * 1024)  # Convert to GB
        folder_data[subdirectory]['size'] = f"{zip_file_size:.2f} GB"
    else:
        folder_data[subdirectory]['size'] = "0 GB"

# Ask the user for the preferred sorting method
sorting_method = input("Enter the sorting method ('name' or 'size'): ")

if sorting_method.lower() == 'name':
    # Sort the folder titles by their names
    sorted_folder_data = {k: v for k, v in sorted(folder_data.items(), key=lambda item: item[1]['title'])}
elif sorting_method.lower() == 'size':
    # Sort the folder titles by the size of the ZIP file in descending order (biggest first)
    sorted_folder_data = {k: v for k, v in sorted(folder_data.items(), key=lambda item: float(item[1]['size'].split()[0]), reverse=True)}
else:
    print("Invalid sorting method. Sorting by name.")
    # Sort the folder titles by their names (default)
    sorted_folder_data = {k: v for k, v in sorted(folder_data.items(), key=lambda item: item[1]['title'])}

# Create a new JSON file to store the sorted folder data
output_file_path = './database.json'
with open(output_file_path, 'w') as output_file:
    json.dump(sorted_folder_data, output_file, indent=4)

print("Folder titles and sizes extracted and saved to", output_file_path)
