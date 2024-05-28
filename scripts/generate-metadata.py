import os
import csv
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from geopy.geocoders import Nominatim

def extract_coordinates(gps_data):
    # Extract latitude and longitude values
    latitude_ref = gps_data.get('GPSLatitudeRef', 'N')
    latitude_degrees, latitude_minutes, latitude_seconds = gps_data.get('GPSLatitude', (0.0, 0.0, 0.0))
    longitude_ref = gps_data.get('GPSLongitudeRef', 'E')
    longitude_degrees, longitude_minutes, longitude_seconds = gps_data.get('GPSLongitude', (0.0, 0.0, 0.0))

    # Convert to decimal degrees
    latitude_decimal = latitude_degrees + latitude_minutes / 60 + latitude_seconds / 3600
    if latitude_ref == 'S':
        latitude_decimal = -latitude_decimal

    longitude_decimal = longitude_degrees + longitude_minutes / 60 + longitude_seconds / 3600
    if longitude_ref == 'W':
        longitude_decimal = -longitude_decimal

    # Return coordinates in standard format
    return float(latitude_decimal), float(longitude_decimal)

# Function to handle the GPS metadata
def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")

            for (t, value) in GPSTAGS.items():
                if t in exif[idx]:
                    geotagging[value] = exif[idx][t]

    return geotagging

# Function to handle the date metadata
def get_date(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")

    date = ""
    for (idx, tag) in TAGS.items():
        if tag == 'DateTime':
            date = exif[idx]

    return date
    
# Function to get location name from coordinates
def get_location_by_coordinates(coordinates):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(coordinates, exactly_one=True)
    address = location.raw['address']
    return address

# Directories to look for images
directories = ['dataset/train/chiki', 'dataset/train/chiki-and-lola', 'dataset/train/lola']

# Check if the CSV file already exists
csv_file_path = 'dataset/train/metadata.csv'
file_exists = os.path.isfile(csv_file_path)

# If the file exists, read it into a list
existing_files = []
if file_exists:
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        try:
          next(reader)  # Skip the header
          existing_files = [row[0] for row in reader]
        except StopIteration:
          pass # File is empty

# Open the CSV file for appending
with open(csv_file_path, 'a', newline='') as file:
    writer = csv.writer(file)
    # Write the header only if the file is empty
    if not file_exists or not existing_files:
      writer.writerow(["file_name", "caption", "date", "location", "coordinates"])

    # Walk through each directory
    for directory in directories:
        for foldername, subfolders, filenames in os.walk(directory):
            for filename in filenames:
                if filename.endswith('.jpg'):
                    file_path = os.path.join(foldername, filename)
                    # Check if the file is already in the CSV
                    if file_path in existing_files:
                        continue  # Skip this file

                    # Open the image file
                    img = Image.open(os.path.join(foldername, filename))
                    # Extract EXIF data
                    exif = img._getexif()
                    
                    try: 
                        # Extract metadata
                        geotagging = get_geotagging(exif)
                        date = get_date(exif)
                        lat, lon = extract_coordinates(geotagging)
                        coordinates = "{}, {}".format(lat, lon)

                        location = get_location_by_coordinates(coordinates)
                    except:
                        # If there is an error, set the metadata to empty
                        geotagging = {}
                        date = ""
                        coordinates = ""
                        location = ""

                    # Write data to CSV
                    writer.writerow([os.path.join(foldername, filename), "", date, location, coordinates])

                    print("Processed: ", os.path.join(foldername, filename))
                    # Close the image file
                    img.close()

print("Metadata generation complete")

                    
                