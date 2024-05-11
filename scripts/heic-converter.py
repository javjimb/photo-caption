import os
import subprocess

def heic_to_jpg(heic_file, jpg_file):
    try:
        subprocess.run(['magick', 'convert', heic_file, jpg_file], check=True)
        os.remove(heic_file)
        print(f"{heic_file} converted and original file deleted.")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {heic_file} to JPG: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

source_path = 'data/heic'
destination_path = 'data/images/jpg'

for file in os.listdir(source_path):
    source_file_path = os.path.join(source_path, file)
    destination_file_path = os.path.join(destination_path, file.split('.')[0] + '.jpg')

    if file.lower().endswith('.heic'):
        heic_to_jpg(source_file_path, destination_file_path)
    elif file.lower().endswith('.jpg') or file.lower().endswith('.jpeg'):
        os.rename(source_file_path, destination_file_path)

print('HEIC to JPG conversion completed!')

