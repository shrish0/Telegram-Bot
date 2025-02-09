from telegram import Update, InputFile
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 🔑 Replace with your actual Telegram bot token

TOKEN = "7371658331:AAEhVWKd28gz_pom91MX1wxfQ9314i-n6Fg"
BOT_USERNAME = "@ShrishResumeBot"
RESUME_PATH = "shrishRes.pdf"  # Ensure this file exists in the bot's directory

# 🏁 Start Command - Introduction Message
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = """👋 Hello Recruiter! Your future employee is here.  
Explore my skills, projects, and resume. Use /help to see all commands."""
    await update.message.reply_text(message)

# 📌 Help Command - List of Available Commands
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    commands = """📌 **Available Commands:**  
📜 **Personal & Academic**  
/personal - View my personal details  
/academic - Check my academic background  
/coursework - See relevant coursework  

💡 **Skills & Achievements**  
/skills - View my technical & soft skills  
/achievements - See my achievements & awards  

🚀 **Projects & Work Experience**  
/projects - Explore my projects  
/experience - View my work experience  

📜 **Certifications & Resume**  
/certifications - Check my certifications  
/resume - Get my resume as a PDF  

💬 **Need Help?**  
/help - Show this command list  
"""
    await update.message.reply_text(commands, parse_mode="Markdown")

# 📜 Resume Command - Sends Resume PDF
async def resume_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        with open(RESUME_PATH, "rb") as resume:
            await update.message.reply_document(document=InputFile(resume), filename="Shrish_Resume.pdf")
    except FileNotFoundError:
        await update.message.reply_text("❌ Resume file not found. Please upload the resume again.")

# 💬 Message Handler - Smart Responses
def handle_response(text: str) -> str:
    text = text.lower()
    if "hello" in text or "hi" in text:
        return "👋 Hey there! How can I help you?"
    elif "who are you" in text:
        return "🤖 I'm ShrishResumeBot, here to showcase my creator's profile!"
    elif "resume" in text:
        return "📜 You can get my resume by typing /resume"
    elif "help" in text:
        return "📌 Use /help to see all available commands."
    return "❓ I'm not sure what you mean. Try using /help to see commands!"

# 📩 Handle Text Messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    response = handle_response(text)
    await update.message.reply_text(response)

# ❌ Error Handling
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Error: {context.error}")

# 🚀 Main Function - Bot Setup
def main():
    app = Application.builder().token(TOKEN).build()

    # Register Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("resume", resume_command))

    # Handle Text Messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Error Handler
    app.add_error_handler(error)

    # Polling (Runs the bot continuously)
    print("🚀 Bot is running...")
    app.run_polling(poll_interval=3)

if __name__ == "__main__":
    main()
