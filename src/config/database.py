from dotenv import load_dotenv, dotenv_values, find_dotenv

import firebase_admin;
from firebase_admin import credentials;
from firebase_admin import firestore;

ENV_DATA = dotenv_values()

FIREBASE_CERT = ENV_DATA.get("FIREBASE_CERT")

print(FIREBASE_CERT)

cred = credentials.Certificate(
    cert= FIREBASE_CERT
);

if cred:
    print("Credential Validity = ", True);

firebaseApp = firebase_admin.initialize_app(credential=cred);
db = firestore.client(firebaseApp);