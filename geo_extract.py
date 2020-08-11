import os
import io
from functools import partial
from geopy.geocoders import Nominatim
from ImageMetaData import ImageMetaData


def get_file_list(path):
    """Get the list of files in a specifc path"""
    files_list = [f for f in os.listdir(path) if (
        os.path.isfile(os.path.join(path, f) and f != '.DS_Store'))]
    return files_list


def heic_to_jpeg(path):
    """
    Convert .HEIC files in a folder to the standard picture format
    .jpg. This is needed because the iOS pictures standard when
    transfered is in .HEIC format and it's not yet supported by
    Python's 'pillow' library.
    """
    files_list = get_file_list(path)
    count = 0

    for img in files_list:
        name, ext = os.path.basename(img).split('.')

        if ext.lower() == 'heic':
            s = io.BytesIO()
            pi = Image.frombytes()


    if count:
        print(f"{count} images successfully converted to .jpg")
        return img_list
    else:
        return files_list


path_name = os.path.join(os.getcwd(), 'pictures')
img_list = heic_to_jpeg(path_name)
img_location_list = []

for img in img_list:
    img_path = os.path.join(path_name, img)
    meta_data = ImageMetaData(img_path)
    lat, lon = meta_data.get_lat_lon()

    img_location_list.append({'filename': img,
                              'file_path': img_path,
                              'latitude': lat,
                              'longitude': lon})


geolocator = Nominatim(user_agent="geo_pic_finder")
reverse = partial(geolocator.reverse, language="en")

location = reverse([lat, lon])
print(location.raw)
