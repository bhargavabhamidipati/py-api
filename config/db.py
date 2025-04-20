import pyrebase
from contextlib import contextmanager
from flask import current_app

firebaseConfig = {
  "apiKey": "AIzaSyCEFGMlYcskFI1Fr2xwJ9XIcC68p2l84oA",
  "authDomain": "flask-project-services.firebaseapp.com",
  "databaseURL": "https://flask-project-services-default-rtdb.firebaseio.com",
  "projectId": "flask-project-services",
  "storageBucket": "flask-project-services.firebasestorage.app",
  "messagingSenderId": "754163693367",
  "appId": "1:754163693367:web:9b690822cc1246bc378cb2",
  "measurementId": "G-JKHVZNFXVW"
}


@contextmanager
def get_db_connection():

    try:
        firebase = pyrebase.initialize_app(firebaseConfig)
        db = firebase.database()
        yield db
    except Exception as e:
        current_app.logger.error(f'Database error: Unable to initialize database connection')


