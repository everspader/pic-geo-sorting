import os
import io
from functools import partial
from geopy.geocoders import Nominatim
from ImageMetaData import ImageMetaData
from PIL import Image
import pyheif
import filetype
import exifread


def get_file_list(path):
    """Get the list of files in a specifc path"""
    files_list = [f for f in os.listdir(path) if (
        os.path.isfile(os.path.join(path, f)) and f != '.DS_Store')]
    return files_list




    if count:
        print(f"{count} images successfully converted to .jpg")
        return get_file_list(path)
    else:
        return files_list


path_name = os.path.join(os.getcwd(), 'pictures')
# img_list = heic_to_jpeg(path_name)
img_list = get_file_list(path_name)
# TO DO: Filter only JPG files
img_data_list = []

geolocator = Nominatim(user_agent="geo_pic_finder")
reverse = partial(geolocator.reverse, language="en")

for img in img_list:
    name, ext = os.path.splitext(img)
    img_path = os.path.join(path_name, img)

    if ext.lower() != '.heic':
        meta_data = ImageMetaData(img_path)
        lat, lon = meta_data.get_lat_lon()
        location = reverse([lat, lon])
        breakpoint()
        country = location.raw['address']['country']

    img_data_list.append({'filename': img,
                          'filetype': ext,
                          'file_path': img_path,
                          'metadata': meta_data,
                          'latitude': lat,
                          'longitude': lon,
                          'country': country})

# location = reverse([lat, lon])
# print(location.raw['address']['country'])
print(img_location_list)
