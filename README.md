# Telegram.com bot in Python - Seed Project

- [Telegram.com bot in Python - Seed Project](#telegramcom-bot-in-python---seed-project)
    - [Introduction](#introduction)
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

## Let's begin

## Create a Telegram bot

The very first thing is creating a bot for having a *token*. You can register your own bot by following the instructions at [Telegram.org](https://core.telegram.org/bots#3-how-do-i-create-a-bot) (you can read the full guide for learning a bit more about bots and everything about what can the do for you).

If you want to deploy your bot as a webhook, you have to register it via Telegram api with the following call (the URL can be even pasted in your browser and it'll work):
`https://api.telegram.org/botYOUR:BOT_TOKEN/setWebhook?url=https://example.com/YOUR:BOT_TOKEN`

`YOUR:BOT_TOKEN` is the token that BotFather has assigned to your bot. `https://example.com` is your domain (it can be an IP if you don't have a domain name).

**Important:** you have to take into account two things:
1. Your domain **has to be https**. Telegram does not allow bots in non-https environments. The good news are that the certificate you use can be a self-signed one. You can also use a free [letsencrypt](https://letsencrypt.org/) certificate.
2. In this guide we assume that you have your bot listening in `https://example.com/YOUR:BOT_TOKEN` rather than just in `https://example.com/`. That's why we believe that making your bot listen in just a domain leaves it *open* to anyone son anyone can send your bot fakes updates. This guide also assumes that you have a reverse proxy that allows you to deploy an arbitrary number of bots on the same domain. If this is not your case, you can also use this project deploying only one bot per domain (or IP) and per allowed port. Remember that as [setWebhook](https://core.telegram.org/bots/api#setwebhook) documentation says, it currently supports 80, 443, 88 and 8443 pors. This allows you to deploy up to four bots per domain without needing any reverse proxy.

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
PORT = '443'
URL_PATH = TOKEN # This is recommended for avoiding random people making fake updates to your bot
KEY = 'certs/private.key'
CERT = 'certs/cert.pem'
WEBHOOK_URL = f'https://example.com/{TOKEN}'
```

- **TOKEN**: Your bot's token. You have to edit this and place the token that BotFather gave to your bot.
- **NAME**: Your bot's name. Optional. This is used for identifying your bot in places like the log file.
- **WEBHOOK**: If set to True, you will have to edit the other configuration options, for making a full-working webhook bot. If you just want to deploy a standard bot that automatically polls to the Telegram [getUpdates](https://core.telegram.org/bots/api#getupdates) method, leave it to False.
- **IP**: The IP your bot will be listening on. Usually you'll leave it a 0.0.0.0 as your bot will be listening on localhost.
- **PORT**: The port your bot will be listening on. If you have a reverse proxy you'll leave it to 443. If not, you'll change it to the port on which you want your bot to listen on (remember you only can choose between 80, 443, 88 and 8443).
- **URL_PATH**: The path you setted in the setWebhook call. It is recommended to leave it equal to your bot's token, but you can change it if you want.
- **KEY**: The path to the private key file you generated if you generated a self-signed certificated o the private key you got if you bought a certificate (or generated a letsencrypt one).
- **CERT**: The path to your .pem file that was generated the same way as your key file.
- **WEBHOOK_URL**: Your full webhook URL. Normally here you'll just edit the domain name. But you can edit the full URL if you want.

## Begin implementing your commands
Implementing new commands is easy, but you might want to take a look at the [python-telegram-bot documentation](https://python-telegram-bot.org/). Now you are quite an expert at python-telegram bot, let's see how to implement new commands.

First, create your command file at the `bot/` directory. For example `bot/start.py`. This file will hold all of your command code. The second thing you have to do is... yes, implement your command logic. I'll give you an example for the *start* command:
```python
def main(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
```

For now this project only supports adding `CommandHandler`. We will add all of the [other handlers](https://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.html#handlers) in the future.

All of your commands functions will receive the same three arguments, [bot](https://python-telegram-bot.readthedocs.io/en/latest/telegram.bot.html) which is the actual bot, [update](https://python-telegram-bot.readthedocs.io/en/latest/telegram.update.html) which holds all the data from the incoming update and `args`, which is an array with the text sent by the user (if any) splitted by spaces. So if you want to rebuild the user input you'll have to do `args.join(' ')`.

The last step is to register your new command in the `commands.py` file. First I'll give you an example of the `commands.py` file with the `/start` command already registered and then I'll explain it to you:
```python
from bot.start import main as start

commands = [
    {
        "command": 'start',
        "function": start
    }
]
```

We begin by importing our command function (in our example, `start.py > main`) an assigning it an alias by doing:
```python
from bot.start import main
```
And then create a new item in the commands array with a dictionary holding two keys, `command` and `function`:
```python
commands = [
    {
        "command": '',
        "function": 
    }
]
```

The first key is the actual command to which your bot will respond, but without the slash (in our example `'start'`). The second one is the function you implemented for handling that command inside the `.py` file (in our  example, `main`). So our commands array will look like:
```python
commands = [
    {
        "command": 'start',
        "function": main
    }
]
```

If you want to register another command just import its file and add it to the commands array, e.g.
```python
from bot.start import main as start
from bot.another_command import main as another_command

commands = [
    {
        "command": 'start',
        "function": start
    },
    {
        "command": 'another',
        "function": another_command
    }
]
```
And you're done! Repeat that process once per new command and the `main.py` will take care of adding one `CommandHandler` for every command you registered without bothering you.

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