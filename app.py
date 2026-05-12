import os
import re
import subprocess
import uuid

from flask import Flask, request, render_template, jsonify, send_from_directory
from werkzeug.utils import secure_filename

from config import UPLOAD_DIR, IMAGE_DIR, DRAFTS_DIR
from file_utils import get_categories, validate_article_path
from nav_builder import rebuild_nav, update_index

app = Flask(__name__)

os.makedirs(IMAGE_DIR, exist_ok=True)
os.makedirs(DRAFTS_DIR, exist_ok=True)


@app.route('/edit-list')
def edit_list():
    """列出所有已有文章，按分类分组。"""
    from file_utils import scan_articles
    articles = scan_articles()
    articles = [(title, category, rel_path) for _, title, category, rel_path, _ in articles]
    articles.sort(key=lambda x: (x[1], x[0]))
    return render_template('list.html', articles=articles)


@app.route('/load_article')
def load_article():
    """返回指定文章的内容，用于编辑器加载。"""
    filepath = request.args.get('path', '')
    full_path = validate_article_path(filepath)
    if not full_path:
        return jsonify({'error': '文件不存在'}), 404
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return jsonify({'content': content, 'title': os.path.splitext(os.path.basename(filepath))[0]})


@app.route('/delete_article', methods=['POST'])
def delete_article():
    """删除指定的文章文件。"""
    filepath = request.form.get('path', '')
    full_path = validate_article_path(filepath)
    if not full_path:
        return jsonify({'error': '文件不存在'}), 404
    try:
        os.remove(full_path)
        rebuild_nav()
        update_index()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/upload_image', methods=['POST'])
def upload_image():
    """接收粘贴的图片，保存到 docs/images，返回 Markdown 链接。"""
    file = request.files.get('image')
    if not file:
        return jsonify({'error': '没有图片'}), 400

    ext = os.path.splitext(secure_filename(file.filename))[1] or '.png'
    filename = f"{uuid.uuid4().hex}{ext}"
    file.save(os.path.join(IMAGE_DIR, filename))
    return jsonify({'url': f"/images/{filename}"})


def _normalize_content(content):
    """规范化 Markdown 内容：统一换行、去首尾空白、压缩连续空行。"""
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    content = content.strip()
    content = re.sub(r'\n{3,}', '\n\n', content)
    return content


def _save_image(image_file):
    """保存上传的图片，返回 Markdown 图片语法字符串。"""
    if not image_file or not image_file.filename:
        return ''
    ext = os.path.splitext(secure_filename(image_file.filename))[1]
    filename = f"{uuid.uuid4().hex}{ext}"
    image_file.save(os.path.join(IMAGE_DIR, filename))
    return f'![](/images/{filename})'


def _git_deploy(title):
    """执行 git add/commit/push。"""
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', f'发布 {title}'])
    subprocess.run(['git', 'push'])


@app.route('/', methods=['GET', 'POST'])
def editor():
    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        content = _normalize_content(request.form['content'])
        is_publish = request.form.get('publish') == 'on'

        image_md = _save_image(request.files.get('image'))

        if image_md:
            md_content = f'# {title}\n\n{image_md}\n\n{content}\n'
        else:
            md_content = f'# {title}\n\n{content}\n'

        if is_publish:
            edit_path = request.form.get('edit_path', '').strip()
            if edit_path:
                old_full_path = os.path.join(UPLOAD_DIR, edit_path)
                old_category = os.path.dirname(edit_path)

                if old_category != category:
                    new_dir = os.path.join(UPLOAD_DIR, category)
                    os.makedirs(new_dir, exist_ok=True)
                    filename = os.path.basename(edit_path)
                    new_path = os.path.join(new_dir, filename)
                    with open(new_path, 'w', encoding='utf-8') as f:
                        f.write(md_content)
                    if os.path.exists(old_full_path):
                        os.remove(old_full_path)
                else:
                    with open(old_full_path, 'w', encoding='utf-8') as f:
                        f.write(md_content)

                rebuild_nav()
                update_index()
            else:
                target_dir = os.path.join(UPLOAD_DIR, category)
                os.makedirs(target_dir, exist_ok=True)
                save_path = os.path.join(target_dir, f'{title}.md')
                with open(save_path, 'w', encoding='utf-8') as f:
                    f.write(md_content)
                rebuild_nav()
                update_index()

            _git_deploy(title)
            return '<script>alert("发布成功！");location.href="/";</script>'
        else:
            draft_path = os.path.join(DRAFTS_DIR, f'{title}.md')
            with open(draft_path, 'w', encoding='utf-8') as f:
                f.write(md_content)
            return '<script>alert("已保存到草稿箱");location.href="/";</script>'

    return render_template('editor.html', categories=get_categories())


@app.route('/create_category', methods=['POST'])
def create_category():
    name = request.form.get('name', '').strip()
    if not name:
        return jsonify({'error': '分类名不能为空'}), 400
    if not re.match(r'^[\w\u4e00-\u9fff-]+$', name):
        return jsonify({'error': '分类名包含非法字符'}), 400
    target = os.path.join(UPLOAD_DIR, name)
    if os.path.exists(target):
        return jsonify({'error': '分类已存在'}), 409
    os.makedirs(target, exist_ok=True)
    return jsonify({'success': True, 'category': name})


@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(IMAGE_DIR, filename)


if __name__ == '__main__':
    app.run(debug=True)
