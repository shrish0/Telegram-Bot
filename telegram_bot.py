import os
from dotenv import load_dotenv
from telegram import Update, InputFile
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
RESUME_PATH = os.getenv("RESUME_PATH")

BOT_USERNAME = "@ShrishResumeBot"

# 🏁 Start Command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = """👋 Hello Recruiter! Your future employee is here.  
Explore my skills, projects, and resume. Use /help to see all commands."""
    await update.message.reply_text(message)

async def certifications_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    certifications = """📜 **Certifications**  
✅ **Machine Learning (ML)** | NPTEL | 📅 Oct 2024  
✅ **Data Analytics with Python** | NPTEL | 📅 Jan-Apr 2024  
✅ **Getting Started With Competitive Programming** | NPTEL | 📅 Jul-Oct 2024  
✅ **Data Structure and Algorithms Using Java** | NPTEL | 📅 Jul-Oct 2023  
"""
    await update.message.reply_text(certifications, parse_mode="Markdown")


# 📌 Help Command - List of Commands
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

# 📜 Resume Command
async def resume_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        with open(RESUME_PATH, "rb") as resume:
            await update.message.reply_document(document=InputFile(resume), filename="Shrish_Resume.pdf")
    except FileNotFoundError:
        await update.message.reply_text("❌ Resume file not found. Please upload the resume again.")

    
async def personal_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    personal_info = """👤 **Shrish Gupta**  
📍 **Location:** Noida, India  
📞 **Phone:** +91 8178160448  
📧 **Email:** [shrishgupta1234@gmail.com](mailto:shrishgupta1234@gmail.com)  

🔗 **LinkedIn:** [Shrish Gupta](https://www.linkedin.com/in/shrish-gupta-9957b422a/)  
📂 **GitHub:** [shrish0](https://github.com/shrish0)  
📸 **Instagram:** [sh_ri_sh_](https://www.instagram.com/sh_ri_sh_/)  
"""
    await update.message.reply_text(personal_info, parse_mode="Markdown")

# 🔥 Message Handler (Responding to Messages)
def handle_response(text: str) -> str:
    text = text.lower()
    if "hello" in text:
        return "👋 Hey there!"
    elif "hi" in text:
        return "😊 Hi! How can I assist you?"
    elif "who are you" in text:
        return "🤖 I'm ShrishResumeBot, here to showcase my creator's profile!"
    return "❓ I'm not sure what you mean. Try using /help to see commands!"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    response = handle_response(text)
    await update.message.reply_text(response)

async def academic_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    academic_info = """🎓 **Education**  
        🏫 **B.Tech in Computer Science and Engineering**  
        📍 *Dr. A.P.J Abdul Kalam Technical University*  
        📍 *IMS Engineering College, Ghaziabad*  
        📅 *Graduation: June 2025*  
        📊 *GPA: 8.546 / 10.0*  

        🏫 **Maharshi Vidya Mandir**  
        📅 *12th Grade (2021) – 86.80%*  
        📅 *10th Grade (2019) – 85.67%*  
        """
    await update.message.reply_text(academic_info, parse_mode="Markdown")


async def skills_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    skills_info = """💻 **Technical Skills**  

            ✅ **Programming (5000+ lines):**  
            - Python, Java, JavaScript, React.js, Django, Node.js, Express  
            - Data Structures & Algorithms  

            ✅ **Programming (1000+ lines):**  
            - C, Selenium, Pandas, TensorFlow, PHP, MySQL, Numpy  

            ✅ **Familiar With:**  
            - Docker, Linux, Tableau, Postman  

            🛠 **Soft Skills**  
            ✅ Time Management  
            ✅ Adaptability  
            ✅ Emotional Intelligence  
            ✅ Critical Thinking  
            """
    await update.message.reply_text(skills_info, parse_mode="Markdown")

async def achievements_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    achievements_info = """🏆 **Achievements**  

🥇 **TCS CodeVita Season 12**  
   - *Round 2 Qualifier (Rank 859 out of thousands)*  

🥇 **1st Place** – *Youth4Future Hackathon (2024)*  
   - *Competed among 45 teams and secured 1st place*  

🥈 **2nd Place** – *Brewing Codes 2.0 Hackathon (2024)*  
   - *Competed among 60 teams and secured 2nd place*  
"""
    await update.message.reply_text(achievements_info, parse_mode="Markdown")

async def coursework_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coursework_info = """📚 **Relevant Coursework**  

✅ **Computer Science & Engineering:**  
   - Data Analytics  
   - Microprocessors  
   - Operating Systems  
   - Database Management System  
   - Artificial Intelligence  
   - Data Structures & Algorithms in C  
"""
    await update.message.reply_text(coursework_info, parse_mode="Markdown")

    
async def projects_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    projects_info = """🛠 **Projects**  

1️⃣ **ShrishResumeBot** *(Python, Telegram API)*  
   - A Telegram bot that shares resume details, projects, and achievements.  

2️⃣ **EDUBOT** *(HTML, CSS, JavaScript, Django, MySQL, Selenium, BS4)*  
   - Voice-controlled website automation integrating Google Search, YouTube, and ChatGPT.  

3️⃣ **Carpooling Web App** *(MERN, Tailwind, DaisyUI)*  
   - A ride-sharing platform that connects users on the same route.  

4️⃣ **Admin Dashboard** *(ASP.NET MVC, Bootstrap, MS SQL 2022)*  
   - A dashboard for managing products, orders, and users in an e-commerce platform.  

5️⃣ **Agri Core** *(Django, MySQL, TensorFlow, Bootstrap)*  
   - A web app for plant disease detection, crop yield prediction, and farmer e-commerce integration.  
"""
    await update.message.reply_text(projects_info, parse_mode="Markdown")


async def experience_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    experience_info = """💼 **Work Experience**  

🔹 **Full Stack Developer Intern** – *Maharshi Ayurveda Pvt Ltd (July 2024, Noida)*  
   - Developed a **Business Workflow Management System** using **ASP.NET MVC**.  
   - Implemented **role-based user management** for secure access control.  
   - Designed **Category and Sub-Category CRUD operations** with bulk import/export using **ClosedXML**.  
   - Built a **robust requisition approval/rejection workflow** to streamline internal processes.  
"""
    await update.message.reply_text(experience_info, parse_mode="Markdown")

# ❌ Error Handling
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Error: {context.error}")

# 🚀 Main Function (Bot Setup)
def main():
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("certifications", certifications_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("resume", resume_command))
    app.add_handler(CommandHandler("personal", personal_command))
    app.add_handler(CommandHandler("academic", academic_command))
    app.add_handler(CommandHandler("skills", skills_command))
    app.add_handler(CommandHandler("achievements", achievements_command))
    app.add_handler(CommandHandler("coursework", coursework_command))
    app.add_handler(CommandHandler("projects", projects_command))
    app.add_handler(CommandHandler("coursework", coursework_command))






    # Message Handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Error Handler
    app.add_error_handler(error)

    # Polling
    print("🚀 Bot is running...")
    app.run_polling(poll_interval=3)

if __name__ == "__main__":
    main()
