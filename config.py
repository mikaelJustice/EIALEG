"""
Configuration settings for the Football League application
"""
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'school-football-league-secret-2024')
    DATABASE = os.path.join(os.path.dirname(__file__), 'instance', 'football.db')
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB max upload
    ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    SESSION_PERMANENT = False
