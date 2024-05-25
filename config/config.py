from datetime import timedelta
import os

config = os.environ.get

class Config:
    SECRET_KEY = config("SECRET_KEY") or "660652117f2951272aa25cfe8dbc540c"
    SQLALCHEMY_DATABASE_URI = config("SQLALCHEMY_DATABASE_URI") or "sqlite:///faxmachine.db"
    JSON_SORT_KEYS = config("JSON_SORT_KEYS") or False
    WTF_CSRF_ENABLED = config("WTF_CSRF_ENABLED") or False

    JWT_SECRET = config("JWT_SECRET") or "660652117f2951272aa25cfe8dbc540c"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=int(config("JWT_ACCESS_TOKEN_EXPIRES") or 2))
    JWT_ACCESS_CSRF_HEADER_NAME = config("JWT_ACCESS_CSRF_HEADER_NAME") or "Authorization"
