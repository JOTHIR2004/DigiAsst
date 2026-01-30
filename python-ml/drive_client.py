import os
import json
from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

load_dotenv()

SCOPES = os.getenv("SCOPES", "").split(",")

credentials = None

# ✅ Render / Production (env-based)
service_account_json = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")

if service_account_json:
    credentials = service_account.Credentials.from_service_account_info(
        json.loads(service_account_json),
        scopes=SCOPES
    )

# ✅ Local development (file-based)
else:
    SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")

    if not SERVICE_ACCOUNT_FILE:
        raise ValueError("SERVICE_ACCOUNT_FILE not set")

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    )

drive_service = build("drive", "v3", credentials=credentials)
