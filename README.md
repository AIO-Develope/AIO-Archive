
<h1 align="center">
    AIO Archive
    <br>
    <div align="center">
    <img src="https://img.shields.io/badge/Python-3.10.4-blue" align="center"/>
    <img src="https://img.shields.io/badge/discord.py-2.1.1-orange" align="center"/>
    <img src="https://img.shields.io/badge/Flask-2.0.1-yellow" align="center"/>
    <img src="https://img.shields.io/badge/Developing-Active-brightgreen" align="center"/>
    <img src="https://img.shields.io/badge/Version-1.0-green" align="center"/>
    </div>
</h1>

This project is a Discord bot that facilitates the retrieval and download of files based on specific codes sent via direct messages. It uses a web server to serve the files and provides users with download links, titles, descriptions, and optional thumbnail images.

# Example
<img src="https://github.com/AIO-Develope/AIO-Archive/assets/69240351/97ff720a-fa16-4fef-8f7f-7b7d254d13bb" width="40%" height="40%"/>

# Installation
```
discord.py==2.1.1
Flask==2.0.1
```
To install the requirements run:
```
pip install -r requirements.txt
```

Now rename ```example.config.json``` to config.json and change the informations to youre desire.

```
{
    "token": "youre token",
    "prefix": "!",
    "webserver": "the domain or ip to youre webserver",
    "archive-path": "./archive"
}
```
1. now you create youre first Archive:
```
python create.py  // run the script
```
2. Enter youre Archive informations:
```
Enter the title: Youre Archive Titel
Enter the description: Description of this Archive
```
3. Now you get this:
```
A new folder 'the archive id' was created in 'youre archive folder' with the message.json file.
```
4. Now you need to put youre archive as a .zip file in the folder you created earlier. (the folder is in youre archive folder and is named by the id)
6. Run the bot with ```python main.py```
7. Now you can access the post by sending the id per dm.

<img src="https://github.com/AIO-Develope/AIO-Archive/assets/69240351/97ff720a-fa16-4fef-8f7f-7b7d254d13bb" width="40%" height="40%"/>

# Optional
You can add a thumpnail to the embed. Just add a thumpnail.png to the archive folder

Now the Folder should like this:
```
ID of Archive
├── archive.zip
├── message.json
└── thumpnail.png
```

# Extra Tools
1. Simple Reading of the Archive. It puts it in ```database.json```. Run it like this:
```
python read.py
```
Now the database.json should look like this:
```
{
    "5238": "Cool Archive",
    "8120": "Nice software",
    "3194": "Photoshop Template Pack",
    "5637": "Sample Titel",
    "2432": "Youre Archive Titel"
}
```

2. Now the advanced way to read the Archive:
```
python read_a.py
Enter the sorting method ('name' or 'size'):          // here you can decide between sorting by name or size
```
Now the database.json should look like this:
```
{
    "5238": {
        "title": "Cool Archive",
        "size": "0.7 GB"
    },
    "8120": {
        "title": "Nice software",
        "size": "0.4 GB"
    },
    "3194": {
        "title": "Photoshop Template Pack",
        "size": "1.2 GB"
    },
    "5637": {
        "title": "Sample Titel",
        "size": "1.1 GB"
    },
    "2432": {
        "title": "Youre Archive Titel",
        "size": "2.3 GB"
    }
}
```
This project is just a randome upload i will not focus on it! but if someone ask for an improvement i will hear it.
