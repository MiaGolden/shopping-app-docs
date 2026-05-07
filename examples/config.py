import os

BASE_URL = os.getenv("API_BASE_URL", "https://api.shopapp.com")
TIMEOUT = int(os.getenv("API_TIMEOUT", 5))
