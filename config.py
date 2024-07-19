# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21857983")

API_HASH = os.environ.get("API_HASH", "e469e84c943ce3b8b056eb6a296f2c67")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7289060685:AAEfteCWvdrQoNZ2JPstVPnBv9Rql_iaLBA") 

FORCE_SUB = os.environ.get("FORCE_SUB", "everythinghappensf0rareason") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://yogesh:vFojzRVGQQKWNmoj@master.2cdyk37.mongodb.net/?retryWrites=true&w=majority&appName=MASTER")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '833465134').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
