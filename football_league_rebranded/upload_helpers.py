"""
Shared helper for handling image uploads.
"""
import os, uuid
from werkzeug.utils import secure_filename
from flask import current_app


ALLOWED = {'png', 'jpg', 'jpeg', 'gif', 'webp'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED


def save_image(file, subfolder):
    """
    Save an uploaded image file to static/uploads/<subfolder>/.
    Returns the URL path like '/uploads/news/abc123.jpg' or None if no file.
    """
    if not file or file.filename == '':
        return None
    if not allowed_file(file.filename):
        return None
    ext = file.filename.rsplit('.', 1)[1].lower()
    filename = f"{uuid.uuid4().hex}.{ext}"
    dest_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], subfolder)
    os.makedirs(dest_dir, exist_ok=True)
    file.save(os.path.join(dest_dir, filename))
    return f'/uploads/{subfolder}/{filename}'


def delete_image(url):
    """Delete an uploaded image by its URL path."""
    if not url:
        return
    try:
        rel = url.lstrip('/')  # e.g. uploads/news/abc.jpg
        full = os.path.join(os.path.dirname(__file__), 'static', rel)
        if os.path.exists(full):
            os.remove(full)
    except Exception:
        pass
