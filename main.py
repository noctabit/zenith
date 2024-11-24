import logging
from telethon import TelegramClient
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
    # Crear cliente de Telethon
    client = TelegramClient(SESSION, API_ID, API_HASH)

    # Registrar mensaje al iniciar el bot
    logger.info("Bot está a punto de iniciar...")

    # Iniciar el cliente con el token del bot
    await client.start(bot_token=BOT_TOKEN)

    # Obtener detalles del bot
    me = await client.get_me()

    # Registrar el nombre de usuario del bot
    logger.info(f"Bot {me.username} iniciado con éxito.")

    # Mantener el bot en ejecución hasta que se desconecte
    await client.run_until_disconnected()

# Ejecutar la función startup
if __name__ == "__main__":
    asyncio.run(startup())
