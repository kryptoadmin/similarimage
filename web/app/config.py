import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "5912VCq6Q04bYnTBk5CZ5xmOCnN642NL")
    UPLOAD_DIR = os.path.join("app", "static", "uploads", "images")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024 # 16MB
    ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif"}