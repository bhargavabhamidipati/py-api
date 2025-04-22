import pyrebase
from contextlib import contextmanager
from flask import current_app
import json
import os
import base64

firebase_config_b64 = os.getenv("FIREBASE_CONFIG_B64")
firebase_config_str = base64.b64decode(firebase_config_b64).decode()
firebase_config = json.loads(firebase_config_str)

@contextmanager
def get_db_connection():

    try:
        firebase = pyrebase.initialize_app(firebase_config)
        db = firebase.database()
        yield db
    except Exception as e:
        current_app.logger.error(f'Database error: Unable to initialize database connection')


