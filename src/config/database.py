from dotenv import load_dotenv, dotenv_values, find_dotenv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

ENV_DATA = dotenv_values()

FIREBASE_CERT = ENV_DATA.get("FIREBASE_CERT")

cred = credentials.Certificate(
    cert={
        "type": "service_account",
        "project_id": "geofencing-94da1",
        "private_key_id": "b451bf4e8cea05619bdc1287c84e31b02d43b6ed",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDMUmfLC82Dh+PL\npRrXPKu4JbofgOUB4tRfAMiDoXkqQtnI5Tn0bGGHBptuL3lkzRsl1U3D29r286AL\n1xDBg6AVCchdMqkVn36aOE1K7WtXViP/oxvYsMTR4c6XNLyjkVzA4GKxVL+1GgjD\ntiWsdEx9h4xfBhs1AD3ValZg2h0N5K1iZdG+/HS7rp81g287nAJ14NZH9EHKuFM3\nFFeCx3T2dtbx2b9HyVjag+NjvVXPW9hH5qMBnwsNNHCFvZj5E6Kntq3Dcj3UnTTb\nMDsDLpf6MvGZIhYR0IfqpTK/rDWyjQX2s7phQCYZf/gjuxhlNJH5AkeHNCFjugFq\n9PuLCn6zAgMBAAECggEAEulDqGmeFXZT5rWQOkC9fMH9K/egT/WLMNnf3+hnpbo3\nRx60UlkKXoGFjFls3nVqIFfRpqGoRCLWJZJmf3Vr29aidWyAIDtkGpPAela8Oy1Y\nD/asV/jl1q6UPQQ0EN2eR08yw0qz+GgBof+vaqVUWRVdMC8JVfVWQ8pfq/+JdeS8\ni5rbWqD3Yo6abjr/2sB2/JCqyPpH3xvNaPs9EMqrvIhV3VwNoAp2Dfj3e1PaNMwm\nw3TSkajm/p2872lKyWliszV2ulVK+qGUQ/qy2ezn3pCq6fuXWP5nhuivdu0Hjfov\nY73XehH9g0AV7uLIS3jtdOADjiNgsEAh9eAURhmb5QKBgQD5JKAmjmZTJLR7s1lZ\n88z7xXOlX0ue0fxCFCNyUQuTiIRKAivf9VucFJCM0fZ1hHwJ6V4hl4remB12bj95\nel0B5vpZ39FJ0za5nYxeQ0pWfBhDNOUcxHhWvtf6eUfIddh7GV2qt9w9WBbj6zHc\nJcrjqpps4aiZwaI5viDAYgXTXQKBgQDR8fxS+IbL8Y+DB30PEONqGwMjxTZDoZ57\nPtadUf0TsUJZCee4VgFawhhU4Du6vTBOkn1ACq+RXYtdgMnAJDNT7J0LHh1wymgV\nHNXYde7bi0NdylewV7Oue0FI+dI2kbF0ABhbeiUM675ZxDwmXlMZEZA7V77bUUfR\n41cgVRAJTwKBgHW99WHDUmBgrFr5e3SjX3Bs9CZnTtmT619fHRFdc9cZYUuIkyuY\nTN8KaPXkFFGddvFINJAzihGAWgwqNh020tWfTxlCSSpWgzpdVoUF0A/nPaAlU1Gx\nGB4GuxNIVcBK0S/74ORZV+A1zTuRX1LnGWdWrPxf+MoRVJVtYRUKPi6RAoGAE5/Z\nBDBy+TFVRtw2VmgvucVYn8lZbyz2UXLoQMBfNa4GE6iXXmW7rq4h9B0ZuDTjBRUw\nXAIjsyTZWB4nvawkmB2v+FASVG63F/IgEyHC+Aamf2fgln08MH0Y9ydS/QLVYZB4\ntmROfkyy+FUdgkCi5976anGjR4Drg7UKed05qIUCgYBqq4e+mp8k8JjkrfXEywZM\nQrBoEv1klBplfCiQ7yOa8dZ6WCVt6aa+jZScZeArvVvGwxhuOp9NrBZiAD3VTLVW\npMfUc/yKwUAy2ivzF8xM3wyLztA+VpUdoQ9436X/w787tHPL6kZyjdLuGjxg8Zcb\nMEWa5mF2/LTpFzQMeWdnQw==\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-wym1l@geofencing-94da1.iam.gserviceaccount.com",
        "client_id": "108052814670134719223",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-wym1l%40geofencing-94da1.iam.gserviceaccount.com",
    }
)

if cred:
    print("Credential Validity = ", True)

firebaseApp = firebase_admin.initialize_app(credential=cred)
db = firestore.client(firebaseApp)
