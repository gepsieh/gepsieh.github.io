import os
import re
from collections import OrderedDict

from mkdocs.plugins import event_priority

MAX_LEN = 28

STYLE = """<style>
  .index-toc { margin: 12px 0; padding: 10px; background: #f5f5f5; border-radius: 4px; }
  .index-toc b { margin-right: 8px; }
  .index-toc a { display: inline-block; margin: 2px 6px; text-decoration: none; color: #2980b9; }
  .index-toc a:hover { text-decoration: underline; }
  .link-grid { display: grid; grid-template-columns: 1fr 1fr; margin-bottom: 8px; }
  .link-grid a { display: block; padding: 4px 10px; border-bottom: 1px solid #f0f0f0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; text-decoration: none; color: #2980b9; }
  .link-grid a:hover { background: #e8f4fd; }
  h3 { margin-top: 12px; margin-bottom: 4px; }
</style>
"""


def generate_index(docs_dir, category):
    src_dir = os.path.join(docs_dir, '米游社相关', category)
    if not os.path.isdir(src_dir):
        return

    files = sorted([
        f for f in os.listdir(src_dir)
        if f.endswith('.md') and f != 'index.md'
    ])

    grouped = OrderedDict()
    for f in files:
        m = re.match(r'(\d{4})-(\d{2})', f)
        if m:
            year, month = m.group(1), m.group(2)
            grouped.setdefault(year, OrderedDict()).setdefault(month, []).append(f)

    lines = [f'# {category}\n', f'共 {len(files)} 篇文章：\n', STYLE, '\n']

    # TOC
    years = list(grouped.keys())
    lines.append('<div class="index-toc">\n<b>目录：</b>\n')
    for y in years:
        lines.append(f'<a href="#y{y}">{y}</a>\n')
    lines.append('</div>\n\n')

    # Each year
    for year in years:
        lines.append(f'<h2 id="y{year}">{year} 年</h2>\n')
        for month in grouped[year]:
            month_files = grouped[year][month]
            lines.append(f'<h3>{int(month)} 月</h3>\n')
            lines.append('<div class="link-grid">\n')
            for f in month_files:
                original_name = re.sub(r'^\d{4}-\d{2}-', '', f[:-3])
                name = original_name if len(original_name) <= MAX_LEN else original_name[:MAX_LEN] + '…'
                html_f = f[:-3] + '.html'
                lines.append(f'<a href="{html_f}">{name}</a>\n')
            lines.append('</div>\n')
        lines.append('\n')

    index_path = os.path.join(src_dir, 'index.md')
    new_content = ''.join(lines)
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as fh:
            old_content = fh.read()
        if old_content == new_content:
            return
    with open(index_path, 'w', encoding='utf-8') as fh:
        fh.write(new_content)


@event_priority(100)
def on_config(config):
    """Regenerate index pages before MkDocs collects files."""
    docs_dir = config['docs_dir']
    for category in ['公告', '活动', '资讯']:
        generate_index(docs_dir, category)
