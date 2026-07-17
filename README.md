# Image Sharpen & Grayscale Batch Processor

A simple Python script that batch-processes all images in a folder — sharpening each one and converting it to grayscale.

## What it does

For every image in the `./img` directory, the script:
1. Applies a sharpening filter
2. Converts the image to grayscale ('L' mode)
3. Saves the result as a `.jpg` in `./final_img`, with `_edited` appended to the original filename

Example: `photo.png` → `./final_img/photo_edited.jpg`

## Requirements

- Python 3.x
- [Pillow](https://pillow.readthedocs.io/) (PIL fork)

Install dependencies:
```
pip install Pillow
```

 All processed images will appear in `./final_img`.
