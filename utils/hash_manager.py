
import bcrypt
from dotenv import load_dotenv
import os

load_dotenv()

class HashManager:

    @staticmethod
    def create_hash(text: str) -> str:
        salt_rounds = int(os.getenv('SALT_ROUNDS', '12'))
        return bcrypt.hashpw(
            text.encode('utf-8'), 
            bcrypt.gensalt(salt_rounds)
        ).decode('utf-8')


    @staticmethod
    def verify_hash(text: str, hashed_text: str) -> bool:
        return bcrypt.checkpw(text.encode('utf-8'), hashed_text.encode('utf-8'))