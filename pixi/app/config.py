import os
from dotenv import load_dotenv


load_dotenv()


class Config:
DATABASE_URL = os.getenv('DATABASE_URL')
JWT_SECRET = os.getenv('JWT_SECRET') or 'please-change-me'
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM') or 'HS256'
JWT_EXP_SECONDS = int(os.getenv('JWT_EXP_SECONDS') or 3600)
TESTING = os.getenv('TESTING', '0') == '1'