from environs import Env


def main_envs(path: str):
    env = Env()
    env.read_env(path)

    return {
        # Telegram Bot Envs
        'bot_name': env.str("BOT_NAME"),
        'bot_token': env.str("BOT_TOKEN"),
        'admin_id': env.int("BOT_ADMIN_ID"),
        # PostgreSQL Envs
        'db_name': env.str("POSTGRES_DB"),
        'db_user': env.str("POSTGRES_USER"),
        'db_pass': env.str("POSTGRES_PASSWORD"),
        'db_host': env.str("POSTGRES_HOST"),
    }


envs = main_envs('.env')
