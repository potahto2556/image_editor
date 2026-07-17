from PIL import Image, ImageEnhance, ImageFilter
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'img')
path_out = os.path.join(script_dir, 'final_img')

os.makedirs(path_out, exist_ok=True)

for filename in os.listdir(path):
    img = Image.open(os.path.join(path, filename))
    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    clean_name = os.path.splitext(filename)[0]
    edit.save(os.path.join(path_out, f"{clean_name}_edited.jpg"))
