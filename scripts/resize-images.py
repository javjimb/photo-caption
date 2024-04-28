import os
from PIL import Image

input_dir = './data/images/original'
output_dir = './data/images/resized'
desired_size = (224, 224) 

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in os.listdir(input_dir):
    filepath = os.path.join(input_dir, filename)
    with Image.open(filepath) as img:
        # Calculate aspect ratio
        aspect_ratio = img.width / img.height

        # Calculate new height based on desired width
        new_width = desired_size[0]
        new_height = int(new_width / aspect_ratio)

        # Resize image while preserving aspect ratio
        resized_img = img.resize((new_width, new_height))
        
        # If you want to pad the resized image to fit the desired size exactly
        # padded_img = Image.new("RGB", desired_size)
        # padded_img.paste(resized_img, ((desired_size[0] - new_width) // 2, (desired_size[1] - new_height) // 2))

        # Save resized image
        resized_img.save(os.path.join(output_dir, filename))

print('Done resizing images')
