"""
School Football League - Main Application Entry Point
Initializes Flask app, registers blueprints, and sets up database
"""

from flask import Flask, redirect, url_for
from config import Config
from database import init_db
from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.captain import captain_bp
from routes.public import public_bp
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Ensure instance folder exists for SQLite DB
    os.makedirs(app.instance_path, exist_ok=True)

    # Ensure upload folders exist
    upload_base = app.config['UPLOAD_FOLDER']
    os.makedirs(os.path.join(upload_base, 'news'), exist_ok=True)
    os.makedirs(os.path.join(upload_base, 'players'), exist_ok=True)

    # Serve uploaded files
    from flask import send_from_directory
    @app.route('/uploads/<path:filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    # Initialize database (creates tables if they don't exist)
    with app.app_context():
        init_db(app)

    # Register all route blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(captain_bp, url_prefix='/captain')
    app.register_blueprint(public_bp)

    # Add enumerate as Jinja2 filter and global
    app.jinja_env.filters['enumerate'] = enumerate
    app.jinja_env.globals['enumerate'] = enumerate

    # Format datetime objects to string for templates
    def format_dt(value):
        if value is None:
            return ''
        if hasattr(value, 'strftime'):
            return value.strftime('%Y-%m-%d %H:%M')
        return str(value)[:16]

    app.jinja_env.filters['fmtdt'] = format_dt

    # Root redirect to home
    @app.route('/')
    def index():
        return redirect(url_for('public.home'))

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
