import sqlite3
import os
import mysql.connector as mysql

# pipenv install python-dotenv
from dotenv import load_dotenv

# db = sqlite3.connect('aula-20210505.db')
# cursor = db.cursor()

load_dotenv()

db = mysql.connect(
    host=os.getenv('DATABASE_HOST'),
    user=os.getenv('DATABASE_USER'),
    passwd=os.getenv('DATABASE_PASSWD')
)

cursor = db.cursor(buffered=True)
