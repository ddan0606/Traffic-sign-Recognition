# -*- coding: utf-8 -*-
"""Duplicate.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M2nRl3MIWATmWuaa55Sj6FInQrwk8rS4
"""

pip install imagehash pillow

import os
from PIL import Image
import imagehash

# Đường dẫn tới thư mục chứa ảnh
folder_path = "/content/drive/MyDrive/4th/Deep Learning/Project/Test_4/GTSRB_1/4"

# Đường dẫn tới thư mục lưu các ảnh không trùng
output_folder = "/content/drive/MyDrive/4th/Deep Learning/Project/Test_4/GTSRB_2/4"

# Tạo thư mục đầu ra nếu nó không tồn tại
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Tạo một từ điển để lưu các ảnh trùng nhau
duplicate_images = {}

# Lặp qua tất cả các tệp tin trong thư mục
for filename in os.listdir(folder_path):
    # Kiểm tra xem tệp tin có phải là ảnh hay không
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Tạo đường dẫn đầy đủ tới tệp tin
        image_path = os.path.join(folder_path, filename)

        # Mở ảnh bằng PIL
        image = Image.open(image_path)

        # Tính hash cho ảnh
        image_hash = imagehash.average_hash(image)

        # Kiểm tra xem hash đã tồn tại trong từ điển chưa
        if image_hash in duplicate_images:
            # Nếu đã tồn tại, xóa tệp tin
            os.remove(image_path)
        else:
            # Nếu chưa tồn tại, lưu hash và tên tệp tin vào từ điển
            duplicate_images[image_hash] = filename
            # Di chuyển tệp tin không trùng vào thư mục đầu ra
            new_image_path = os.path.join(output_folder, filename)
            os.rename(image_path, new_image_path)
