import os
from PIL import Image

def compress_image(input_path, output_path, target_size_kb=100, dpi=(300, 300)):
    img = Image.open(input_path)
    img.save(output_path, dpi=dpi, quality=85)
    
    while os.path.getsize(output_path) > target_size_kb * 1024:
        img = Image.open(output_path)
        img = img.resize((int(img.size[0] * 0.9), int(img.size[1] * 0.9)), Image.LANCZOS)
        img.save(output_path, dpi=dpi, quality=85)

def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    total_files = sum([len(files) for _, _, files in os.walk(input_folder)])
    processed_files = 0
    
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, input_folder)
                output_path = os.path.join(output_folder, relative_path)
                
                output_dir = os.path.dirname(output_path)
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                
                compress_image(input_path, output_path)
                processed_files += 1
                print(f'Processed {processed_files}/{total_files} files')

input_folder = './resource'
output_folder = './compressed'
process_folder(input_folder, output_folder)
print('Done!')