import numpy as np
from PIL import Image
import os

def preprocess_images(input_dir: str, output_dir: str, size=(128, 128)):
    """
    Preprocess the images in the input directory by resizing them to a consistent resolution,
    and normalizing pixel values. Save the preprocessed images to the output directory.

    Args:
        input_dir (str): Path to the directory containing original images.
        output_dir (str): Path to the directory where preprocessed images will be saved.
        size (tuple): Desired resolution to resize images to.
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through images in the input directory
    for filename in os.listdir(input_dir):
        input_filepath = os.path.join(input_dir, filename)
        
        # Load image
        image = Image.open(input_filepath)

        image_array = np.array(image)

        # Normalize between 0-1
        image_array = image_array / 255.0

        # Save as .npy to retain float values
        np.save(os.path.join(output_dir, os.path.splitext(filename)[0]), image_array)

# Example usage
if __name__ == "__main__":
    original_images_dir = './data/images/resized'
    preprocessed_images_dir = './data/images/normalized'
    preprocess_images(original_images_dir, preprocessed_images_dir)