# Telegram.com bot in Python - Seed Project

- [Telegram.com bot in Python - Seed Project](#telegramcom-bot-in-python---seed-project)
    - [Introduction](#introduction)
    - [Project structure](#project-structure)
    - [Let's begin](#lets-begin)
    - [First things first](#first-things-first)
    - [Create a Telegram bot](#create-a-telegram-bot)
    - [Installing dependencies](#installing-dependencies)
    - [Edit config file](#edit-config-file)
    - [Begin implementing your commands](#begin-implementing-your-commands)
    - [Feedback and new ideas](#feedback-and-new-ideas)
    - [License](#license)

## Introduction

This bot is intended to be used as a template for telegram bots in Python. The goal of this project is to facilitate and speed up the bot developing process.

This project has been developed using Python 3.7 (but is compatible with, at least, python 3.5) and assumes that you use [pipenv](https://docs.pipenv.org/) as dependency manager.

The project uses as the underlying technology [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).

The project also allows you to deploy the bot as a webhook or as a polling bot.

## Project structure
```bash
.
├── assets
├── bot
│   ├── start.py
│   └── test.py
├── configurations
│   └── config.py
├── connectors
│   └── __init__.py
├── logs
│   └── seed_bot.log
├── utils
│   └── logger.py
├── LICENSE
├── main.py
├── Pipfile
├── Pipfile.lock
└── README.md
```

Let's see how is this project structured:
- assets: Here you will place all your assets files such as icons, images, audio and video files, etc.
- bot: Here you will place all your bot [command](#begin-implementing-your-commands) files.
- configurations: As it name says, this folder will contains all of your bot configuration files.
- connectors: This folder is intented to hold any connector your bot will need (such as databases, APIs, ect.)
- logs: Pretty self-explanatory, just the logs folder.
- utils: Here you will place any of your bot utils files. For example, files containing sets of helper functions.
- LICENSE: Just the license file you may want to change it for your project.
- main.py: The project entry point.
- Pipfile and Pipfile.lock: Dependencies files used by pipenv.
- README.md: This file.

## Let's begin

## First things first
First of all, clone this repository and remove the .git folder, so you can begin developing your bot in your own repo.

## Create a Telegram bot

The very first thing is creating a bot for having a *token*. You can register your own bot by following the instructions at [Telegram.org](https://core.telegram.org/bots#3-how-do-i-create-a-bot) (you can read the full guide for learning a bit more about bots and everything about what can they do for you).

**NOTE**: Even if you want to deploy your bot as a webhook, you don't have to register it via Telegram API because python-telegram-bot and this project will do it for you.

**Important:** you have to take into account two things:
1. Your domain **has to be https**. Telegram does not allow bots in non-https environments. The good news are that you can use a self-signed certificate. You can also use a free [letsencrypt](https://letsencrypt.org/) certificate.
2. In this guide we assume that you have your bot listening in `https://example.com/YOUR:BOT_TOKEN` rather than just in `https://example.com/`. That's because we believe that making your bot listen in just a domain leaves it *open* to anyone so anyone can send your bot fakes updates. This guide also assumes that your server allows you to deploy an arbitrary number of bots on the same domain, e.g. having one bot on `https://example.com/path/to/bot1` and another on `https://example.com/path/to/bot2`... If this is not your case, you can also use this project deploying only one bot per domain (or IP) and per allowed port. Remember that as [setWebhook](https://core.telegram.org/bots/api#setwebhook) documentation says, it currently supports only 80, 443, 88 and 8443 pors. This allows you to deploy up to four bots per domain without needing any reverse proxy.

## Installing dependencies

Now that you (surely) have pipenv installed, you just have to run 
```bash
pipenv install
```
from the project directory

## Edit config file

The default config file placed at `configurations/bot_config.py` has the following default content:
```python
TOKEN = "bot:T0K3N"
NAME = "seed_bot"
WEBHOOK = True
## The following configuration is only needed if you set WEBHOOK to True ##
IP = '0.0.0.0'
PORT = 443
URL_PATH = TOKEN # This is recommended for avoiding random people making fake updates to your bot
WEBHOOK_URL = 'https://example.com/%s' % (URL_PATH,)
```

- **TOKEN**: Your bot's token. You have to edit this and place the token that BotFather gave to your bot.
- **NAME**: Your bot's name. Optional. This is used for identifying your bot in places like the log file.
- **WEBHOOK**: If set to True, you will have to edit the other configuration options, for making a full-working webhook bot. If you just want to deploy a standard bot that automatically polls to the Telegram [getUpdates](https://core.telegram.org/bots/api#getupdates) method, leave it to False.
- **IP**: The IP your bot will be listening on. Usually you'll leave it a 0.0.0.0 as your bot will be listening on localhost.
- **PORT**: The port your bot will be listening on. If you don't have a reverse proxy you'll leave it to 443 (or any other supported port like 80, 88 or 8443). If you have a reverse proxy, you'll change it to the port on which you want your bot to listen on. After that, you have to configure your reverse proxy to redirect all incoming traffic from https://example.com/TOKEN to IP:PORT.
- **URL_PATH**: The path you set in the setWebhook call. It is recommended to leave it equal to your bot's token, but you can change it if you want.
- **WEBHOOK_URL**: Your full webhook URL. Normally here you'll just edit the domain name. But you can edit the full URL if you want.

## Begin implementing your commands
Implementing new commands is easy, but you might want to take a look at the [python-telegram-bot documentation](https://python-telegram-bot.org/).

Now that you are quite an expert at python-telegram bot, let's see how to implement new commands.

You just have to create a file that will hold all your command functionality. Let's take a closer look at this process.

Imagine you want to implement a `start` command. First, create your command file at the `bot/` directory. It is not required, but we recommend you to name the file as your command. As the command would be `start` is a good idea to name the file `start` too, i.e. `bot/start.py`. This file will hold all of your command code. The only requirement is that your command file has to implement a **at least** an `init` function. So the second thing you have to do is... yes, implement your command logic.

All main functions from command files receive the same argument, the *dipatcher*. This way, you can implement any type of command. I'll give you an example for the *start* command:
```python
def init(dispatcher): # A main function is mandatory
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

def start(bot, update): # You can structure your code in any numbers of functions that you can call from the main one
    bot.send_message(
        chat_id=update.message.chat_id, 
        text="I'm a bot, please talk to me!"
    )
```

And you're done. Next time you launch your bot, it'll respond to the `/start` command.


## Feedback and new ideas
Feel free to give me some feedback or new ideas to improve the project. If you have any suggestions please feel free to create an [issue](https://github.com/alesanmed/python-telegram-bot-seed/issues) and tag it as `enhancement`

## License
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org>
