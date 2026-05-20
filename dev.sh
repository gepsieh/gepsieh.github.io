#!/bin/bash
# 本地调试脚本
# 用法: ./dev.sh          → 启动 mkdocs serve，打开浏览器 (热重载)
#       ./dev.sh test     → 启动并在 URL 加 ?test 运行冒烟测试
#       ./dev.sh build    → 增量构建 site/ (只重建变更文件)

echo "📝 启动本地开发服务器..."
echo "   MkDocs 地址: http://127.0.0.1:8000"
echo "   编辑页地址: http://127.0.0.1:8000/admin/"
echo ""

if [ "$1" = "test" ]; then
  echo "🧪 页面加载后将自动运行冒烟测试"
  SMOKE="?test"
fi

if [ "$1" = "build" ]; then
  echo "🔨 增量构建 site/ ..."
  mkdocs build --dirty
  exit
fi

if command -v xdg-open &>/dev/null; then
  (sleep 3 && xdg-open "http://127.0.0.1:8000/admin/${SMOKE}") &
elif command -v open &>/dev/null; then
  (sleep 3 && open "http://127.0.0.1:8000/admin/${SMOKE}") &
fi

mkdocs serve -a 127.0.0.1:8000
