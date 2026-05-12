import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, 'mkdocs.yml')
UPLOAD_DIR = os.path.join(BASE_DIR, 'docs')
IMAGE_DIR = os.path.join(UPLOAD_DIR, 'images')
DRAFTS_DIR = os.path.join(BASE_DIR, 'drafts')
IGNORED_DIRS = {'images', 'javascripts'}
INDEX_LIMIT = 10
