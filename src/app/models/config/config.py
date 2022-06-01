import firebase_admin
from firebase_admin import firestore
credentials = firebase_admin.credentials.Certificate("src/app/models/config/models-4ae2e-firebase-adminsdk-7v3f2-e07740eeee.json")
default_app = firebase_admin.initialize_app(credentials)

db = firestore.client()