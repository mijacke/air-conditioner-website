import os

class Config:
    DEBUG = os.environ.get("FLASK_DEBUG", False)
    SECRET_KEY = os.environ.get("SECRET_KEY", "your-secret-key")
    ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS", "https://air-conditioners-website.vercel.app")
