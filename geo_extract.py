import os
import io
from functools import partial
from geopy.geocoders import Nominatim
from ImageMetaData import ImageMetaData


def get_file_list(path):
    """Get the list of files in a specifc path"""
    files_list = [f for f in os.listdir(path) if (
        os.path.isfile(os.path.join(path, f)) and f != '.DS_Store')]
    return files_list

def jpg_img_list(img_list):
    """Return a list of accepted jpg files from the pictures list"""
    jpg_ext = ['.jpg', '.jpeg']
    jpg_list = [img for img in img_list if (
        os.path.splitext(img)[-1].lower() in jpg_ext)]
    return jpg_list


path_name = os.path.join(os.getcwd(), 'pictures')
jpg_img_list = jpg_img_list(get_file_list(path_name))
jpg_img_data_list = []
geolocator = Nominatim(user_agent="geo_pic_finder")
reverse = partial(geolocator.reverse, language="en")

for img in jpg_img_list:
    # name, ext = os.path.splitext(img)
    img_path = os.path.join(path_name, img)

    try:
        meta_data = ImageMetaData(img_path)
        lat, lon = meta_data.get_lat_lon()
        location = reverse([lat, lon])
        country = location.raw['address']['country']
    except:
        pass

    jpg_img_data_list.append({'filename': img,
                          'file_path': img_path,
                          'metadata': meta_data,
                          'latitude': lat,
                          'longitude': lon,
                          'country': country})

print(jpg_img_data_list)
