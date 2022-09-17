import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
    INSTA_USERNAME = os.environ.get('INSTA_USERNAME', None)
    INSTA_PASSWORD = os.environ.get('INSTA_PASSWORD', None)
else:
    # Fill the Values
    API_ID = 10658300
    API_HASH = "728e3bfb3598067c562f86451ef811f2"
    BOT_TOKEN = "5785161589:AAHog_lU0cKFcTtGa_FN4L5kwRZz4hQE6uU"
    DATABASE_URL = ""
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "StarkBots"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
    INSTA_USERNAME = "inst.anathan"
    INSTA_PASSWORD = "CR2000"
