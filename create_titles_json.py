#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
创建仅包含标题的轻量级JSON文件
用于加速主页章节列表加载
"""

import json
import os

def create_titles_json():
    """从完整的TEXT.json中提取标题，创建轻量级titles.json"""
    
    # 检查原始文件是否存在
    if not os.path.exists('TEXT.json'):
        print("错误：找不到TEXT.json文件")
        return False
    
    try:
        # 读取完整的章节数据
        with open('TEXT.json', 'r', encoding='utf-8') as f:
            full_data = json.load(f)
        
        # 提取标题信息
        titles_data = []
        for i, chapter in enumerate(full_data):
            titles_data.append({
                "index": i,
                "title": chapter.get("title", ""),
                "has_content": bool(chapter.get("text", "").strip())
            })
        
        # 保存轻量级标题文件
        with open('titles.json', 'w', encoding='utf-8') as f:
            json.dump(titles_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 成功创建 titles.json")
        print(f"📊 共处理 {len(titles_data)} 个章节")
        print(f"📁 文件大小对比：")
        print(f"   - TEXT.json: {os.path.getsize('TEXT.json') / 1024 / 1024:.2f} MB")
        print(f"   - titles.json: {os.path.getsize('titles.json') / 1024:.2f} KB")
        print(f"🚀 加载速度提升: {os.path.getsize('TEXT.json') / os.path.getsize('titles.json'):.0f}倍")
        
        return True
        
    except Exception as e:
        print(f"❌ 处理失败: {e}")
        return False

if __name__ == "__main__":
    print("🚀 开始创建轻量级标题文件...")
    success = create_titles_json()
    
    if success:
        print("\n🎉 创建完成！现在可以：")
        print("1. 手动运行此脚本更新标题数据")
        print("2. 主页将加载titles.json实现秒级显示")
        print("3. 阅读时仍然使用完整的TEXT.json")
    else:
        print("\n❌ 创建失败，请检查TEXT.json文件是否存在")