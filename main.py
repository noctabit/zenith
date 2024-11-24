import logging
from pyrogram import Client
from configs import API_ID, API_HASH, BOT_TOKEN, SESSION
import asyncio

# Configuración del logger solo para consola
logging.basicConfig(
    level=logging.INFO,  # Definir el nivel de log como INFO
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato del log
    handlers=[logging.StreamHandler()]  # Solo salida en consola
)

# Obtener el logger
logger = logging.getLogger(__name__)

async def startup():
    # Crear cliente de Pyrogram para el bot usando una sesión específica
    client = Client(SESSION, api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

    # Registrar mensaje al iniciar el bot
    logger.info("Bot está a punto de iniciar...")

    # Iniciar el cliente
    await client.start()

    # Obtener detalles del bot
    me = await client.get_me()

    # Registrar el nombre de usuario del bot
    logger.info(f"Bot {me.username} iniciado con éxito.")

    # Mantener el bot en ejecución
    await client.idle()  # Usamos 'idle' para mantener el bot en ejecución

# Ejecutar la función startup
if __name__ == "__main__":
    asyncio.run(startup())
