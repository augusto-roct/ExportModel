import firebase_admin
from firebase_admin import firestore
import os

credentials = {}

try:
    credentials= firebase_admin.credentials.Certificate("src/app/models/config/env.json")
except:
    credentials["type"]= os.environ["TYPE"]
    credentials["project_id"]= os.environ["PROJECT_ID"]
    credentials["private_key_id"]= os.environ["PRIVATE_KEY_ID"]
    credentials["private_key"]= os.environ["PRIVATE_KEY"]
    credentials["client_email"]= os.environ["CLIENT_EMAIL"]
    credentials["client_id"]= os.environ["CLIENT_ID"]
    credentials["auth_uri"]= os.environ["AUTH_URI"]
    credentials["token_uri"]= os.environ["TOKEN_URI"]
    credentials["auth_provider_x509_cert_url"]= os.environ["AUTH_PROVIDER_X509_CERT_URL"]
    credentials["client_x509_cert_url"]= os.environ["CLIENT_X509_CERT_URL"]
    
default_app = firebase_admin.initialize_app(credentials)

db = firestore.client()