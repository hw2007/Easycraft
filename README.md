# Easycraft
A simple Minecraft: Java Edition server manager for Mac &amp; Linux

# Features
* Simple to use, command line interface
* Start, stop, & restart servers easily
* Backup servers, and delete old backups to save space
* Restore a backup with one command! No need to unzip, delete files, and move files yourself.
* All configurable to meet your needs!

# Installing
You will need to have python 3 installed to your system. If you are on mac, it should come pre-installed.
To check if you have python, run <code>python3 -V</code> in a terminal. If you get an error, you do not have python installed.

Installing python differs depending on your system, but if you have [Homebrew](https://brew.sh/) installed, simply run:

<code>brew install python3</code> 

Once you have python installed, you can simply download the latest release on the right, and get started!

# Setup
To get started, navigate to the directory that contains the easycraft.sh file in a terminal, and run <code>./easycraft.sh config</code> to open the config file in vim.

Here you can setup a *binding* for your server. A binding is a way of telling Easycraft where your server(s) are located, and what they should be called.

Find the "bindings" section of the config. It should be at the top.
<img width="1230" alt="image" src="https://github.com/hw2007/Easycraft/assets/60082961/419fd43d-bf69-44e8-8245-9a3c1ba2a032">

Now edit the binding (you'll need to press I to enter insert mode). If your server's launch jar file is located at "~/minecraft/my_server/server-launch.jar", and you want your server to be referred to as "my_server", you would edit the binding like so:
<img width="1219" alt="image" src="https://github.com/hw2007/Easycraft/assets/60082961/207e426a-20e5-4b9d-a737-ccecbec5755c">

Before you exit the config file, you might want to change the default backups directory. It should be the next option after bindings. Simply add the full path to wherever you want backups to be stored. Do not put a forward slash at the end of the path.

Alright, now press ESC, and then type <code>:wq</code> to save & exit the config file. You are now ready to get started!

# Usage
The script has a help page, so I won't list the commands here. Type <code>./easycraft.sh help</code> to open it!

If you need more info for some flags or you want to change the default behaviour of something, checkout the config file!

If you want to automate tasks, such as backing up the server once a day, you can use crontab! Look up a quick tutorial on how to use that if you want to.
