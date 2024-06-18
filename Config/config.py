import os
import dotenv

dotenv.load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
TARGET_ACCOUNTS = os.getenv("TARGET_ACCOUNTS")

if TARGET_ACCOUNTS:
    TARGET_ACCOUNTS = TARGET_ACCOUNTS.split(",")
else:
    TARGET_ACCOUNTS = []

if not USERNAME or not PASSWORD:
    raise ValueError("USERNAME and PASSWORD must be set in the .env file")
if not TARGET_ACCOUNTS:
    raise ValueError("TARGET_ACCOUNTS must be set in the .env file")
