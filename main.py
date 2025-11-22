import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Токен бота (будет установлен в Railway)
TOKEN = os.environ.get('TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатывает команду /start"""
    user = update.effective_user
    await update.message.reply_text(
        f"🌙 Привет, {user.first_name}!\n\n"
        "Я бот-интерпретатор снов. Опиши мне свой сон, и я помогу его разобрать!"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатывает текстовые сообщения"""
    user_message = update.message.text
    user = update.effective_user

    # Простой анализ сна
    text_lower = user_message.lower()
    response = f"🔮 {user.first_name}, вот анализ твоего сна:\n\n"

    if 'лес' in text_lower:
        response += "🌲 *Лес* - символ твоего подсознания и неизведанного.\n"
    if 'вода' in text_lower or 'река' in text_lower:
        response += "💧 *Вода* - отражает твое эмоциональное состояние.\n"
    if 'луна' in text_lower:
        response += "🌙 *Луна* - связана с интуицией и тайнами.\n"
    if 'полет' in text_lower or 'летать' in text_lower:
        response += "🕊️ *Полет* - означает стремление к свободе.\n"

    # Если не найдено ключевых слов
    if response == f"🔮 {user.first_name}, вот анализ твоего сна:\n\n":
        response += "💭 Пока я умею анализировать только определенные символы (лес, вода, луна, полет). Опиши сон подробнее!"

    response += "\n✨ Этот сон записан в нашу базу!"
    await update.message.reply_text(response)

def main():
    """Запускает бота"""
    application = Application.builder().token(TOKEN).build()

    # Обработчики команд и сообщений
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
