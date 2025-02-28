from psycopg2 import connect
from cryptography.fernet import Fernet
import os

conn = connect(os.getenv('DATABASE_URL'), sslmode='require')
fernet = Fernet(os.getenv('SECRET_KEY'))

# get username, password list
def get_users():
    cur = conn.cursor()
    cur.execute("SELECT id, username, password, disco, whatsapp FROM users")
    return [(id, username, fernet.decrypt(password.encode()).decode(), disco, whatsapp) for id, username, password, disco, whatsapp in cur.fetchall()]

