import numpy as np
from PIL import Image, ImageOps
import os

def augment_images(input_dir: str, output_dir: str):
    """
    Apply augmentations to the images in the input directory and save the augmented images to the output directory.

    Args:
        input_dir (str): Path to the directory containing original images.
        output_dir (str): Path to the directory where augmented images will be saved.
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through images in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.npy'):
            input_filepath = os.path.join(input_dir, filename)
            
            # Load image
            image_array = np.load(input_filepath)
            image = Image.fromarray((image_array * 255).astype(np.uint8))

            # Convert RGBA images to RGB
            if image.mode == 'RGBA':
              image = image.convert('RGB')

            # Apply augmentations
            # Rotate image
            image = image.rotate(15)

            # Flip image horizontally
            image = ImageOps.flip(image)

            # Adjust brightness
            image = ImageOps.autocontrast(image)

            # Crop image
            width, height = image.size
            left = width // 4
            top = height // 4
            right = 3 * width // 4
            bottom = 3 * height // 4
            image = image.crop((left, top, right, bottom))

            image_array = np.array(image)

            # Normalize between 0-1
            image_array = image_array / 255.0

            # Save as .npy to retain float values
            np.save(os.path.join(output_dir, filename), image_array)

# Example usage
if __name__ == "__main__":
    normalized_images_dir = './data/images/normalized'
    augmented_images_dir = './data/images/augmented'
    augment_images(normalized_images_dir, augmented_images_dir)