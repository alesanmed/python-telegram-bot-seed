# Telegram.com bot in Python - Seed Project

- [Telegram.com bot in Python - Seed Project](#telegramcom-bot-in-python---seed-project)
    - [Introduction](#introduction)
    - [Project structure](#project-structure)
    - [Let's begin](#lets-begin)
    - [Create a Telegram bot](#create-a-telegram-bot)
    - [Install dependencies](#install-dependencies)
    - [Edit config file](#edit-config-file)
    - [Begin implementing your commands](#begin-implementing-your-commands)
    - [Feedback and new ideas](#feedback-and-new-ideas)
    - [License](#license)

## Introduction

This bot is intended to be used as a template for telegram bots in Python. The goal of this project is to facilitate and speed up the bot developing process.

This project has been developed using Python 3.7 and assumes that you use [pipenv](https://docs.pipenv.org/) as dependency manager.

The project uses as the underlying technology [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).

The project also allows you to deploy the bot as a webhook or as a normal polling bot.

## Project structure
```bash
.
├── assets
├── bot
│   ├── start.py
│   └── test.py
├── configurations
│   └── bot_config.py
├── connectors
│   └── __init__.py
├── logs
│   └── seed_bot.log
├── utils
│   └── logger.py
├── commands.py
├── LICENSE
├── main.py
├── Pipfile
├── Pipfile.lock
└── README.md
```

Let's see how is this project structured:
- assets: Here you will place all your assets files such as icons, images, audio and video files, etc.
- bot: Here you will place all your bot  [command](#begin-implementing-your-commands) files.
- configurations: As it name says, this folder will contains all of your bot configuration files.
- connectors: This folder is intented to hold any connector your bot will need (such as databases, APIs, ect.)
- logs: Pretty self-explanatory, just the logs folder.
- utils: Here you will place any of your bot utils files. For example, files containing sets of helper functions.
- commands.py: This file is used for naming your commands.
- LICENSE: Just the license file
- main.py: The project entry point.
- Pipfile and Pipfile.lock: Dependencies files used by pipenv
- README.md: This file

## Let's begin

## Create a Telegram bot

The very first thing is creating a bot for having a *token*. You can register your own bot by following the instructions at [Telegram.org](https://core.telegram.org/bots#3-how-do-i-create-a-bot) (you can read the full guide for learning a bit more about bots and everything about what can the do for you).

Even if you want to deploy your bot as a webhook, you don't have to register it via Telegram api because python-telegram-bot takes care of it.

**Important:** you have to take into account two things:
1. Your domain **has to be https**. Telegram does not allow bots in non-https environments. The good news are that the certificate you use can be a self-signed one. You can also use a free [letsencrypt](https://letsencrypt.org/) certificate.
2. In this guide we assume that you have your bot listening in `https://example.com/YOUR:BOT_TOKEN` rather than just in `https://example.com/`. That's because we believe that making your bot listen in just a domain leaves it *open* to anyone so anyone can send your bot fakes updates. This guide also assumes that your server allows you to deploy an arbitrary number of bots on the same domain, e.g. having one bot on `https://example.com/path/to/bot1` and another on `https://example.com/path/to/bot2`... If this is not your case, you can also use this project deploying only one bot per domain (or IP) and per allowed port. Remember that as [setWebhook](https://core.telegram.org/bots/api#setwebhook) documentation says, it currently supports 80, 443, 88 and 8443 pors. This allows you to deploy up to four bots per domain without needing any reverse proxy.

## Install dependencies

Now that you (surely) have pipenv installed, you just have to checkout the project and run 
```bash
pipenv install
```
From the project directory

## Edit config file

The default config file placed at `configurations/bot_config.py` has the following default content:
```python
TOKEN = "bot:T0K3N"
NAME = "seed_bot"
WEBHOOK = True
## The following configuration is only needed if you setted WEBHOOK to True ##
IP = '0.0.0.0'
PORT = 443
URL_PATH = TOKEN # This is recommended for avoiding random people making fake updates to your bot
WEBHOOK_URL = f'https://example.com/{TOKEN}'
```

- **TOKEN**: Your bot's token. You have to edit this and place the token that BotFather gave to your bot.
- **NAME**: Your bot's name. Optional. This is used for identifying your bot in places like the log file.
- **WEBHOOK**: If set to True, you will have to edit the other configuration options, for making a full-working webhook bot. If you just want to deploy a standard bot that automatically polls to the Telegram [getUpdates](https://core.telegram.org/bots/api#getupdates) method, leave it to False.
- **IP**: The IP your bot will be listening on. Usually you'll leave it a 0.0.0.0 as your bot will be listening on localhost.
- **PORT**: The port your bot will be listening on. If you don't have a reverse proxy you'll leave it to 443 (or any other supported port like 80, 88 or 8443). If you have a reverse proxy, you'll change it to the port on which you want your bot to listen on. After that, you have to configure nginx to redirect all incoming traffic from https://example.com/TOKEN to IP:PORT.
- **URL_PATH**: The path you setted in the setWebhook call. It is recommended to leave it equal to your bot's token, but you can change it if you want.
- **WEBHOOK_URL**: Your full webhook URL. Normally here you'll just edit the domain name. But you can edit the full URL if you want.

## Begin implementing your commands
Implementing new commands is easy, but you might want to take a look at the [python-telegram-bot documentation](https://python-telegram-bot.org/).

Now that you are quite an expert at python-telegram bot, let's see how to implement new commands.

You just have to create a file named the samy way as your command and implement your command functionality in a function called `main`. Let's take a closer look at this process.

Imagine you want to implement a `start` command. First, create your command file at the `bot/` directory. As the command would be `start` the filename has to be `start` too, i.e. `bot/start.py`. This file will hold all of your command code. The only requirement is that your command file has to implement a **at least** a `main` function. So t the second thing you have to do is... yes, implement your command logic. I'll give you an example for the *start* command:
```python
def main(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
```

For now this project only supports adding `CommandHandler`. We will add all of the [other handlers](https://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.html#handlers) in the future.

All of your commands functions will receive the same three arguments, [bot](https://python-telegram-bot.readthedocs.io/en/latest/telegram.bot.html) which is the actual bot, [update](https://python-telegram-bot.readthedocs.io/en/latest/telegram.update.html) which holds all the data from the incoming update and `args`, which is an array with the text sent by the user (if any) splitted by spaces. So if you want to rebuild the user input you'll have to do `' '.join(args)`.

And you're done. Next time you launch your bot, it'll respont to the `/start` command.

But... what if you want to name your files in some way and the commands implemented by those files in some other way? For that purpose exists the `commands.py` file.

Let's imagine that you want to implement a command named `other`, but you cant to name your command file `test.py`. First, you'll create your `bot/test.py` file with a `main` function inside it implementing all your command's logic. And then you register it in the `commands.py` file this way:

```python
commands = {
    'test': {
        'command': 'other'
    }
}
```

Each file has its own entry. The key has to be the filename of your command, in our example `test`. The value is another dict, with a key `command`. That property will hold your custom command name, in our example `other`.

Next time you launch your bot it'll respond to the command `/other`.

And you're done! The project will take care of adding one `CommandHandler` for every file in your `bot/` folder without bothering you.

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