import os
from dotenv import load_dotenv
load_dotenv()
CHATGPT_TOKEN = os.getenv('CHATGPT_TOKEN')
print(CHATGPT_TOKEN)
print(BOT_TOKEN)