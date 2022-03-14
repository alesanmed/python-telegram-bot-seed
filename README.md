# Telegram.com bot in Python - Seed Project

- [Introduction](#introduction)
- [Project structure](#project-structure)
- [Let's begin](#lets-begin)
- [First things first](#first-things-first)
- [Create a Telegram bot](#create-a-telegram-bot)
- [Installing dependencies](#installing-dependencies)
- [Edit config file](#edit-config-file)
- [Begin implementing your commands](#begin-implementing-your-commands)
- [Feedback and new ideas](#feedback-and-new-ideas)

## Introduction

This bot is a template for telegram bots in Python. The goal is to facilitate and speed up the bot developing process.

This project has been developed using Python 3.7 and assumes that you use [Poetry](https://python-poetry.org/) as the dependency manager.

The project uses [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) as the underlying technology.

The project also allows you to deploy the bot as a webhook or polling bot.

## Project structure
```bash
.
├── assets
├── bot
│   └── start.py
├── configurations
│   └── settings.py
├── connectors
│   └── __init__.py
├── logs
│   └── seed_bot.log
├── utils
│   └── logger.py
├── LICENSE
├── main.py
├── pyproject.toml
├── poetry.lock
└── README.md
```

Let's see how this project is structured:
- assets: All your assets files such as icons, images, audio and video files, etc.
- bot: All your bot [command](#begin-implementing-your-commands) files.
- configurations: All of your bot configuration files.
- connectors: Any connectors your bot will need (such as databases, APIs, etc.)
- logs: Just the logs folder.
- utils: Bot utils files. For example, files containing sets of helper functions.
- LICENSE: Just the license file. You may want to change it for your project.
- main.py: The project entry point.
- pyproject.toml and poetry.lock: Dependencies files used by poetry.
- README.md: This file.

## Let's begin

## First things first
First of all, clone this repository and remove the .git folder. Now you can begin developing your bot in your repo.

## Create a Telegram bot

First, create a bot for having a *token*. You can register your bot by following the instructions at [Telegram.org](https://core.telegram.org/bots#3-how-do-i-create-a-bot) (you can read the guide for learning a bit more about bots and everything about what can they do for you).

**NOTE**: Even if you want to deploy your bot as a webhook, you don't have to register it via Telegram API because python-telegram-bot and this project will do it for you.

**Important:** you have to take into account two things:
1. Your domain **has to be https**. Telegram does not allow bots in non-https environments. The good news is that you can use a self-signed certificate. You can also use a free [letsencrypt](https://letsencrypt.org/) certificate.
2. In this guide, we assume that you have your bot listening in `https://example.com/YOUR:BOT_TOKEN` rather than just in `https://example.com/`. That's because we believe that making your bot listen in just a domain leaves it *open* to anyone so anyone can send your bot fakes updates. This guide also assumes that your server allows you to deploy an arbitrary number of bots on the same domain, e.g. having one bot on `https://example.com/path/to/bot1` and another on `https://example.com/path/to/bot2`... If this is not your case, you can also use this project for deploying only one bot per domain (or IP) as well as per allowed port. Remember that as [setWebhook](https://core.telegram.org/bots/api#setwebhook) documentation says, it currently supports only 80, 443, 88, and 8443 ports. This allows you to deploy up to four bots per domain without a reverse proxy.

## Installing dependencies

Now that you (surely) have poetry installed, run
```bash
poetry install
```
from the project directory

## Edit config file

The default config file placed at `configurations/settings.py` has the following default content:
```python
TOKEN = "bot:Token"
NAME = "seed_bot"
WEBHOOK = False
## The following configuration is only needed if you setted WEBHOOK to True ##
WEBHOOK_OPTIONS = {
    'listen': '0.0.0.0',  # IP
    'port': 443,
    'url_path': TOKEN,  # This is recommended for avoiding random people
                        # making fake updates to your bot
    'webhook_url': f'https://example.com/{TOKEN}'
}
```

- **TOKEN**: Your bot's token. You have to edit this and put the token BotFather gave to your bot.
- **NAME**: Your bot's name. Optional. Identifies your bot in places like the log file.
- **WEBHOOK**: If set to True, you have to edit the other configuration options for making a full-working webhook bot. If you want to deploy a standard bot that automatically polls to the Telegram [getUpdates](https://core.telegram.org/bots/api#getupdates) method, leave it to False.
- **IP**: The IP your bot will be listening to. Usually, you'll leave it a 0.0.0.0 as your bot will be listening on localhost.
- **PORT**: The port your bot will be listening to. If you don't have a reverse proxy you'll leave it to 443 (or any other supported port like 80, 88, or 8443). If you have a reverse proxy, you'll change it to the port you want your bot to listen to. After that, you have to configure your reverse proxy to redirect all incoming traffic from https://example.com/TOKEN to IP:PORT.
- **URL_PATH**: The path you set in the setWebhook call. I recommend leaving it equal to your bot's token, but you can change it if you want.
- **WEBHOOK_URL**: Your full webhook URL. Usually, you'll just edit the domain name. But you can edit the full URL if you want.

## Begin implementing your commands
Implementing new commands is easy, but you might want to look at the [python-telegram-bot documentation](https://python-telegram-bot.org/).

Now that you are an expert at python-telegram bot, let's see how to implement new commands.

You have to create a file that will hold all your command functionality. Let's take a closer look at this process.

Imagine you want to implement a `start` command. First, create your command file in the `bot/` directory. It is not required, but we recommend to name the file as your command. As the command would be `start` is a good idea to name the file `start` too, i.e. `bot/start.py`. This file will hold all of your command code. The only requirement is that your command file has to implement **at least** an `init` function. So the second thing you have to do is implement your command logic.

All main functions from command files receive the same argument, the *dipatcher*. This way, you can implement any type of command. I'll give you an example for the *start* command:

```python
def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(CommandHandler('start', start))


def start(update: Update, context: CallbackContext):
    """Process a /start command."""
    update.message.reply_text(text="I'm a bot, please talk to me!")

```

And you're done. Next time you launch your bot, it'll respond to the `/start` command.


## Feedback and new ideas
Feel free to give me some feedback or new ideas to improve the project. If you have any suggestions please feel free to create an [issue](https://github.com/alesanmed/python-telegram-bot-seed/issues) and tag it as `enhancement`.