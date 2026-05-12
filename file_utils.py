import os

from config import UPLOAD_DIR, IGNORED_DIRS


def scan_articles():
    """扫描 docs 下所有 .md 文件，返回 (文件绝对路径, 标题, 分类, 相对路径, 修改时间) 列表。"""
    articles = []
    for root, dirs, files in os.walk(UPLOAD_DIR):
        if any(ignored in root for ignored in IGNORED_DIRS):
            continue
        for file in files:
            if file.endswith('.md') and file != 'index.md':
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, UPLOAD_DIR)
                title = os.path.splitext(file)[0]
                category = os.path.relpath(root, UPLOAD_DIR)
                if category == '.':
                    category = ''
                mtime = os.path.getmtime(full_path)
                articles.append((full_path, title, category, rel_path, mtime))
    return articles


def get_categories():
    """返回 docs 下所有有效子目录名作为分类列表。"""
    return sorted([
        d for d in os.listdir(UPLOAD_DIR)
        if os.path.isdir(os.path.join(UPLOAD_DIR, d))
        and not d.startswith('.')
        and d not in IGNORED_DIRS
    ])


def validate_article_path(filepath):
    """安全校验：确保路径在 docs 下且是 .md 文件，返回绝对路径或 None。"""
    if not filepath or not filepath.endswith('.md') or '..' in filepath:
        return None
    full_path = os.path.join(UPLOAD_DIR, filepath)
    full_path = os.path.realpath(full_path)
    if not full_path.startswith(os.path.realpath(UPLOAD_DIR)):
        return None
    if not os.path.isfile(full_path):
        return None
    return full_path
