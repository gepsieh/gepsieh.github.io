// 浮动编辑按钮
document.addEventListener('DOMContentLoaded', function() {
  var btn = document.createElement('a');
  btn.href = '/admin/index.html';
  btn.title = '在线编辑';
  btn.style.position = 'fixed';
  btn.style.bottom = '20px';
  btn.style.right = '20px';
  btn.style.width = '56px';
  btn.style.height = '56px';
  btn.style.borderRadius = '50%';
  btn.style.backgroundColor = '#409eff';
  btn.style.color = 'white';
  btn.style.display = 'flex';
  btn.style.alignItems = 'center';
  btn.style.justifyContent = 'center';
  btn.style.fontSize = '24px';
  btn.style.boxShadow = '0 2px 12px rgba(0,0,0,0.2)';
  btn.style.textDecoration = 'none';
  btn.style.zIndex = '9999';
  btn.innerHTML = '+';
  document.body.appendChild(btn);

  // 首页动态加载最近更新
  var el = document.getElementById('recent-updates');
  if (!el) return;

  var API = 'https://api.github.com/repos/gepsieh/gepsieh.github.io/git/trees/main?recursive=1';
  fetch(API)
    .then(function(r) { return r.json(); })
    .then(function(data) {
      var articles = [];
      (data.tree || []).forEach(function(item) {
        if (item.path.indexOf('docs/') !== 0) return;
        var rel = item.path.substring(5);
        if (!rel.endsWith('.md') || rel === 'index.md') return;
        if (rel.indexOf('images/') !== -1) return;
        var parts = rel.split('/');
        var title = parts[parts.length - 1].replace('.md', '');
        articles.push({ title: title, path: rel.replace('.md', '.html') });
      });
      if (!articles.length) { el.textContent = '暂无文章'; return; }
      articles.sort(function(a, b) { return a.title.localeCompare(b.title); });
      if (articles.length > 10) articles = articles.slice(0, 10);

      var html = '<ul>';
      articles.forEach(function(a) {
        html += '<li><a href="' + a.path + '">' + a.title + '</a></li>';
      });
      html += '</ul>';
      el.innerHTML = html;
    })
    .catch(function() {
      el.textContent = '加载失败，请刷新重试';
    });
});
