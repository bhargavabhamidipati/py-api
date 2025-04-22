import pyrebase
from contextlib import contextmanager
from flask import current_app
from .firebase_config import firebase_config

@contextmanager
def get_db_connection():
    """
    Context manager to initialize and yield a Firebase Realtime Database connection.

    Usage:
        with get_db_connection() as db:
            db.child("some_node").get()

    Yields:
        db: Firebase database instance for performing read/write operations.

    Logs:
        - Logs an error if Firebase initialization fails.
    """

    try:
        firebase = pyrebase.initialize_app(firebase_config)
        db = firebase.database()
        yield db
    except Exception as e:
        current_app.logger.error(f'Database error: Unable to initialize database connection')


