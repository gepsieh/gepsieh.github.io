// 浮动编辑按钮
document.addEventListener('DOMContentLoaded', function() {
  var btn = document.createElement('a');
  btn.href = 'http://127.0.0.1:5000';
  btn.target = '_blank';
  btn.title = '打开编辑器';
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
});