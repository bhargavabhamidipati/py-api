import os


firebase_config = {
  "apiKey": str(os.getenv("API_KEY")),
  "authDomain": str(os.getenv("AUTH_DOMAIN")),
  "databaseURL": str(os.getenv("DATABASE_URL")),
  "projectId": str(os.getenv("PROJECT_ID")),
  "storageBucket": str(os.getenv("STORAGE_BUCKET")),
  "messagingSenderId": str(os.getenv("MESSAGING_SENDER_ID")),
  "appId": str(os.getenv("APP_ID")),
  "measurementId": str(os.getenv("MEASUREMENT_ID"))
}