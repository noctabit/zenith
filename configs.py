import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener las variables de entorno
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION = os.getenv("SESSION")

# Verificar que todas las variables estén presentes
if not all([API_ID, API_HASH, BOT_TOKEN, SESSION]):
    raise ValueError("Faltan variables en el archivo .env.")
