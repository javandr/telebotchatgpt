import telebot
import openai

# Здесь необходимо указать токен Telegram Bot API и учетные данные GPT-3 API
TLG_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
GPT3_API_KEY = 'YOUR_GPT3_API_KEY'

# Инициализация клиента GPT-3
openai.api_key = GPT3_API_KEY

# Создание объекта бота Telegram
bot = telebot.TeleBot(TLG_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, готовый отвечать на ваши вопросы. Что бы вы хотели спросить?")

# Обработчик входящих сообщений
@bot.message_handler(content_types=["text"])
def chat(message):
    # Получение ответа на вопрос из GPT-3
    response = openai.Completion.create(
        engine="davinci",
        prompt=message.text,
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # Отправка ответа на вопрос пользователю в Telegram
    bot.send_message(message.chat.id, response.choices[0].text[:4096])

# Запуск бота
bot.polling()

