from passlib.hash import bcrypt
import jwt
from quart import current_app
import asyncio
from datetime import datetime, timedelta




def hash_password(password: str) -> str:
return bcrypt.hash(password)




def verify_password(password: str, hashed: str) -> bool:
return bcrypt.verify(password, hashed)




def create_access_token(subject: dict) -> str:
now = datetime.utcnow()
payload = {
'sub': subject,
'iat': now,
'exp': now + timedelta(seconds=current_app.config['JWT_EXP_SECONDS'])
}
token = jwt.encode(payload, current_app.config['JWT_SECRET'], algorithm=current_app.config['JWT_ALGORITHM'])
# jwt.encode returns str in pyjwt>=2
return token




def decode_token(token: str) -> dict:
try:
payload = jwt.decode(token, current_app.config['JWT_SECRET'], algorithms=[current_app.config['JWT_ALGORITHM']])
return payload
except Exception:
return None