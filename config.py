import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'that-is-the-secret-key'