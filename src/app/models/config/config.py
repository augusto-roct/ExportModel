import firebase_admin
from firebase_admin import firestore
credentials = firebase_admin.credentials.Certificate("src/app/models/config/env.json")
default_app = firebase_admin.initialize_app(credentials)

db = firestore.client()