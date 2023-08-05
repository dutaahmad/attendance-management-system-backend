from dotenv import load_dotenv, dotenv_values, find_dotenv

import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

ENV_DATA = dotenv_values()

FIREBASE_CERT = ENV_DATA.get("FIREBASE_CERT")

print("tipe data FIREBASE_CERT : " + str(type(FIREBASE_CERT)))

FIREBASE_CERT_DICT: dict = json.loads(FIREBASE_CERT)

print("tipe data FIREBASE_CERT_DICT : " + str(type(FIREBASE_CERT_DICT)))

cred = credentials.Certificate(cert=FIREBASE_CERT_DICT)

if cred:
    print("Credential Validity = ", True)

firebaseApp = firebase_admin.initialize_app(credential=cred)
db = firestore.client(firebaseApp)
