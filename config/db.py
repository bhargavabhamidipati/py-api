import pyrebase
from contextlib import contextmanager
from flask import current_app
from firebase_config import firebase_config

@contextmanager
def get_db_connection():

    try:
        firebase = pyrebase.initialize_app(firebase_config)
        db = firebase.database()
        yield db
    except Exception as e:
        current_app.logger.error(f'Database error: Unable to initialize database connection')


