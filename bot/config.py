from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 1747534))
    API_HASH = env.get("TELEGRAM_API_HASH", "5a2684512006853f2e48aca9652d83ea")
    OWNER_ID = int(env.get("OWNER_ID", 5748909356))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "5748909356").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "kumastreamxbot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "6554978132:AAGzmfLaNZKOl3cuRuAgshXdOJInOqNmzKw")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1001924574319))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("drive.bearzap.me", "http://127.0.0.1:8080")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
