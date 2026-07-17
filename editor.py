from PIL import Image, ImageEnhance, ImageFilter
import os

path = './img'
path_out = '/final_img'
# Create the output folder if it doesn't exist yet
os.makedirs(f".{path_out}", exist_ok=True)

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    clean_name = os.path.splitext(filename)[0]
    edit.save(f".{path_out}/{clean_name}_edited.jpg")
