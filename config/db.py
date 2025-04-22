import pyrebase
from contextlib import contextmanager
from flask import current_app
import json
import os

firebase_config_str = os.getenv("FIREBASE_CONFIG")
firebase_config = json.loads(firebase_config_str)

@contextmanager
def get_db_connection():

    try:
        firebase = pyrebase.initialize_app(firebase_config)
        db = firebase.database()
        yield db
    except Exception as e:
        current_app.logger.error(f'Database error: Unable to initialize database connection')


