#!/bin/bash
# 将 docs/images/ 下的图片迁移到按文章分文件夹的存储方式
# 用法：在项目根目录执行 bash scripts/migrate-images.sh

set -e

DOCS="docs"
IMAGES="$DOCS/images"

echo "=== 扫描文章中的图片引用 ==="

# 收集每个文章的图片引用：article-slug -> filenames
declare -A ARTICLE_IMAGES
declare -A FILENAME_TO_SLUG  # 文件名 -> 所属文章（第一个引用的）
declare -A FILENAME_MOVED    # 记录已移动的文件

for md_file in "$DOCS"/**/*.md; do
  [ -f "$md_file" ] || continue
  [ "$md_file" = "$DOCS/index.md" ] && continue

  slug="${md_file#$DOCS/}"
  slug="${slug%.md}"

  # 提取该文章中所有指向 docs/images/ 的图片引用（支持绝对和相对路径）
  references=$(grep -oE '!\[[^]]*\]\([^)]*images/[^)]+\)' "$md_file" 2>/dev/null || true)
  [ -z "$references" ] && continue

  while IFS= read -r ref; do
    # 提取文件名（URL 中最后一个 / 之后、) 之前的部分）
    filename=$(echo "$ref" | grep -oE 'images/([^)]+)' | sed 's|images/||')
    [ -z "$filename" ] && continue

    # 记录文章与图片的关系
    ARTICLE_IMAGES["$slug"]+="$filename"$'\n'

    # 如果该图片尚未分配到某个文章，记录第一个引用的文章
    if [ -z "${FILENAME_TO_SLUG[$filename]}" ]; then
      FILENAME_TO_SLUG["$filename"]="$slug"
    fi
  done <<< "$references"
done

echo ""
echo "=== 创建目标文件夹并移动图片 ==="

# 遍历每个文件-文章映射，移动图片并更新引用
for filename in "${!FILENAME_TO_SLUG[@]}"; do
  slug="${FILENAME_TO_SLUG[$filename]}"
  src="$IMAGES/$filename"
  target_dir="$IMAGES/$slug"
  dst="$target_dir/$filename"

  # 检查源文件是否存在
  if [ ! -f "$src" ]; then
    echo "  [跳过] $src 不存在"
    continue
  fi

  # 创建目标文件夹
  mkdir -p "$target_dir"

  # 移动文件
  echo "  移动: $filename -> $slug/"
  git mv "$src" "$dst" 2>/dev/null || mv "$src" "$dst"
  FILENAME_MOVED["$filename"]=1
done

echo ""
echo "=== 更新文章中的图片引用 ==="

# 更新每个文章文件中的图片路径
for md_file in "$DOCS"/**/*.md; do
  [ -f "$md_file" ] || continue
  [ "$md_file" = "$DOCS/index.md" ] && continue

  slug="${md_file#$DOCS/}"
  slug="${slug%.md}"
  modified=0

  # 获取该文章引用的图片文件名
  imgs="${ARTICLE_IMAGES[$slug]}"

  while IFS= read -r filename; do
    [ -z "$filename" ] && continue

    # 确定该图片实际存放的文章文件夹
    target_slug="${FILENAME_TO_SLUG[$filename]}"
    [ -z "$target_slug" ] && continue

    old_pattern="images/$filename"
    new_path="images/$target_slug/$filename"

    # 检查文件中是否还有旧引用
    if grep -q "$old_pattern" "$md_file" 2>/dev/null; then
      sed -i "s|images/$filename|$new_path|g" "$md_file"
      modified=1
      echo "  更新: $md_file ($filename -> $target_slug/$filename)"
    fi
  done <<< "$imgs"

  # 如果该文章的图片被移动到其他文章下，也需要更新（跨文章引用）
  [ "$modified" -eq 0 ] && continue

done

# 处理跨文章引用的图片：文章A的图片被文章B引用
# 上面已经通过全局替换处理了（sed 在所有文件中替换了该文件名）
# 但还需要检查是否有文章引用了不属于它自己的图片
for md_file in "$DOCS"/**/*.md; do
  [ -f "$md_file" ] || continue
  [ "$md_file" = "$DOCS/index.md" ] && continue

  # 检查文件中是否还有未迁移的 images/ 引用（使用 grep 找出直接指向 images/ 根目录的引用）
  old_refs=$(grep -oE '!\[[^]]*\]\([^)]*images/[^/)]+\)' "$md_file" 2>/dev/null || true)

  [ -z "$old_refs" ] && continue

  while IFS= read -r ref; do
    filename=$(echo "$ref" | grep -oE 'images/([^)/]+)' | sed 's|images/||')
    [ -z "$filename" ] && continue
    target_slug="${FILENAME_TO_SLUG[$filename]}"
    [ -z "$target_slug" ] && continue

    old_pattern="images/$filename"
    new_path="images/$target_slug/$filename"
    echo "  [跨文章] 更新: $md_file ($filename -> $target_slug/$filename)"
    sed -i "s|$old_pattern|$new_path|g" "$md_file"
  done <<< "$old_refs"
done

echo ""
echo "=== 迁移完成 ==="
echo "请检查修改内容，然后 git add 并提交。"
# 列出变更
git status --short "$IMAGES" "$DOCS"/*.md 2>/dev/null || true
