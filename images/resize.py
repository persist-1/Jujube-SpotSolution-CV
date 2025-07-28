# resize_images.py
from PIL import Image
import os

def resize_images(input_dir, output_dir, size=(20, 20)):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # 打开图片文件
            img_path = os.path.join(input_dir, filename)
            with Image.open(img_path) as img:
                # 调整图片大小
                img = img.resize(size, Image.ANTIALIAS)
                # 保存调整后的图片到输出目录
                output_path = os.path.join(output_dir, filename)
                img.save(output_path)
                print(f"Resized and saved {filename} to {output_path}")

if __name__ == "__main__":
    input_directory = r"images\other_icon_v2"  # 输入目录
    output_directory = r"images\rescaled_icons_v2"    # 输出目录
    target_size = (40, 40)      # 目标大小
    
    resize_images(input_directory, output_directory, target_size)