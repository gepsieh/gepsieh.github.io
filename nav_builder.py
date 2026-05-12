import os

from ruamel.yaml import YAML

from config import CONFIG_PATH, UPLOAD_DIR, IGNORED_DIRS, INDEX_LIMIT
from file_utils import scan_articles

yaml = YAML()
yaml.preserve_quotes = True


def update_index(limit=INDEX_LIMIT):
    """扫描所有 .md 文件，生成首页"最近更新"列表。"""
    index_md = os.path.join(UPLOAD_DIR, 'index.md')
    articles = scan_articles()

    articles.sort(key=lambda x: x[4], reverse=True)
    recent = articles[:limit]

    lines = [
        "# 欢迎来到 📚 原神资料库\n",
        "## 🕒 最近更新\n",
    ]
    for _, title, _, rel_path, _ in recent:
        html_path = rel_path.replace('.md', '.html')
        lines.append(f"- [{title}]({html_path})")

    with open(index_md, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


def rebuild_nav():
    """扫描 docs/ 下所有 .md 文件，重新生成 mkdocs.yml 的 nav 结构。"""
    articles = scan_articles()

    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        config = yaml.load(f)

    categories = {}
    for _, _, category, rel_path, _ in articles:
        if category in IGNORED_DIRS:
            continue
        rel_path = rel_path.replace('\\', '/')
        categories.setdefault(category, []).append(rel_path)

    new_nav = []
    root_files = categories.pop('', [])
    for f in sorted(root_files):
        new_nav.append({os.path.splitext(os.path.basename(f))[0]: f})

    for cat in sorted(categories.keys()):
        files = sorted(categories[cat])
        new_nav.append({cat: files})

    config['nav'] = new_nav
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        yaml.dump(config, f)
