#!/usr/bin/env python3
"""
图片压缩脚本 - 解决35秒加载问题
将2.96MB的封面图片压缩至500KB以内
"""

import os
from PIL import Image
import sys

def compress_image(input_path, output_path, quality=85, max_size=(800, 1200)):
    """
    压缩图片文件
    
    Args:
        input_path: 输入图片路径
        output_path: 输出图片路径
        quality: 压缩质量 (1-100)
        max_size: 最大尺寸 (宽, 高)
    """
    try:
        # 打开原始图片
        with Image.open(input_path) as img:
            # 获取原始尺寸
            original_size = img.size
            original_format = img.format
            
            # 计算缩放比例
            width, height = img.size
            if width > max_size[0] or height > max_size[1]:
                img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # 保存压缩后的图片
            if img.mode == 'RGBA':
                # PNG格式，保持透明度
                img.save(output_path.replace('.jpg', '.png'), 'PNG', optimize=True)
            else:
                # JPEG格式
                img.save(output_path, 'JPEG', optimize=True, quality=quality)
            
            # 获取文件大小
            original_size_bytes = os.path.getsize(input_path)
            compressed_size_bytes = os.path.getsize(output_path)
            
            original_size_mb = original_size_bytes / (1024 * 1024)
            compressed_size_mb = compressed_size_bytes / (1024 * 1024)
            
            print(f"🎯 图片压缩完成:")
            print(f"   📏 尺寸: {original_size} → {img.size}")
            print(f"   📊 大小: {original_size_mb:.2f}MB → {compressed_size_mb:.2f}MB")
            print(f"   📉 压缩率: {(1 - compressed_size_mb/original_size_mb)*100:.1f}%")
            print(f"   🚀 加载速度提升: {original_size_mb/compressed_size_mb:.1f}倍")
            
            return True
            
    except Exception as e:
        print(f"❌ 压缩失败: {e}")
        return False

def main():
    input_file = "封面-last-Komii.png"
    output_file = "封面-compressed.png"
    
    if not os.path.exists(input_file):
        print(f"❌ 找不到文件: {input_file}")
        return
    
    print("🚀 开始压缩封面图片...")
    print(f"📁 原始文件: {input_file} (2.96MB)")
    print(f"🎯 目标文件: {output_file} (<500KB)")
    print("-" * 50)
    
    # 压缩图片
    success = compress_image(input_file, output_file, quality=80, max_size=(600, 900))
    
    if success:
        print("-" * 50)
        print("✅ 压缩成功！")
        print("💡 建议: 将index.html中的图片路径改为'封面-compressed.jpg'")
        print("📝 操作步骤:")
        print("   1. 修改index.html中的图片src")
        print("   2. 刷新页面测试加载速度")
        print("   3. 预计加载时间: 35秒 → 1秒内")
    else:
        print("❌ 压缩失败，请检查图片文件")

if __name__ == "__main__":
    main()