# Многофункциональный бот на основе Telegram API и GPT-3 API / Multifunctional bot based on Telegram API and GPT-3 API

Этот код представляет собой мощный бот, который использует возможности Telegram API для связи с пользователями и GPT-3 API для генерации ответов на заданные им вопросы.
This code is a powerful bot that uses the capabilities of the Telegram API to communicate with users and the GPT-3 API to generate responses to questions posed to them.

## Настройка / Configuration

Перед запуском нужно внести следующие изменения в код:

1. Замените в файле `main.py` следующее `YOUR_TELEGRAM_BOT_TOKEN` на токен вашего Telegram бота. Если вы еще не создали бота, пройдите по [этой ссылке](https://core.telegram.org/bots#creating-a-new-bot) и создайте его с помощью BotFather.

2. Замените в файле `main.py` следующее `YOUR_GPT3_API_KEY` на ваш ключ API GPT-3. Если у вас нет ключа API, зарегистрируйтесь на [OpenAI](https://beta.openai.com/signup/) и получите его.

The following code changes must be made before launching:

1. Replace the following `YOUR_TELEGRAM_BOT_TOKEN` in the `main.py` file with your Telegram bot token. If you haven't created a bot yet, go to [this link](https://core.telegram.org/bots#creating-a-new-bot) and create one using BotFather.

2. Replace the following `YOUR_GPT3_API_KEY` in the `main.py` file with your GPT-3 API key. If you don't have the API key, register on [OpenAI](https://beta.openai.com/signup/) and get it.

## Запуск / Startup

После внесения необходимых изменений в код, сохраните файл как `bot.py` и запустите его, используя команду:

```
python bot.py
```

После запуска ваш бот будет зарегистрирован на сервере Telegram и будет готов принимать входящие сообщения и генерировать ответы. Вы можете начать общение с ботом через Telegram, отправив ему текстовое сообщение.

**Примечание**: Убедитесь, что у вас установлен Python 3 и необходимые библиотеки (`telebot` и `openai`). Если вы еще не установили эти библиотеки, выполните следующие команды:

```
pip install telebot
pip install openai
``` 

или 

```
pip3 install telebot
pip3 install openai
``` 

в зависимости от того, какая версия Python у вас установлена на компьютере.

### English

After making the necessary changes to the code, save the file as `bot.py` and run it using the command

```
python bot.py
```

Once launched, your bot will be registered on the Telegram server and ready to accept incoming messages and generate responses. You can start communicating with the bot via Telegram by sending it a text message.

**Note**: Make sure you have Python 3 and the necessary libraries (`telebot` and `openai`) installed. If you haven't already installed these libraries, run the following commands:

```
pip install telebot
pip install openai
``` 

or 

```
pip3 install telebot
pip3 install openai
``` 

depending on which version of Python you have installed on your computer.

## Функциональность / Functionality

Бот реагирует на команду /start и затем ожидает входящих сообщений от пользователей. Как только он получает текстовое сообщение, он использует GPT-3 API для генерации ответа на вопрос и отправляет его обратно пользователю в Telegram.

The bot responds to the /start command and then waits for incoming messages from users. Once it receives a text message, it uses the GPT-3 API to generate an answer to the question and sends it back to the user in Telegram.

## Использование / Using

Вы можете запустить этот бот на своем компьютере или сервере, чтобы его могли использовать другие пользователи Telegram. Просто запустите код и начните общаться с ботом через Telegram.

You can run this bot on your computer or server so other Telegram users can use it. Just run the code and start communicating with the bot via Telegram.

**Примечание**: Перед использованием этого бота убедитесь, что вы имеете соответствующие разрешения на использование Telegram Bot API и GPT-3 API.
**Note**: Before using this bot, make sure you have the appropriate permissions to use the Telegram Bot API and GPT-3 API.
