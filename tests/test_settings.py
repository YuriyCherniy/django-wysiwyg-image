import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    'wysiwyg_img'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

WYSISWYG_IMG_UPLOAD_TO = 'test_folder'
WYSISWYG_IMG_IMAGE_WIDTH = 50