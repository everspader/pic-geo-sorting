import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


class ImageMetaData(object):

    exif_data = None
    image = None

    def __init__(self, img_path):
        self.image = Image.open(img_path)
        self.get_exif_data()
        super(ImageMetaData, self).__init__()

    def get_exif_data(self):
        """
        Return a dictionary of the EXIF metadata from the pictures with tags
        decoded to human readable information
        """
        exif_data = {}
        info = self.image.getexif()

        if info:
            for tag_id, value in info.items():
                tag_decoded = TAGS.get(tag_id, tag_id)
                if tag_decoded == 'GPSInfo':
                    gps_data = {}
                    for t in value:
                        sub_decoded = GPSTAGS.get(t, t)
                        gps_data[sub_decoded] = value[t]

                    exif_data[tag_decoded] = gps_data
                else:
                    exif_data[tag_decoded] = value

        self.exif_data = exif_data
        return exif_data

    def get_if_exist(self, data, key):
        """Return the value of a tag if it exists in the Exif data"""
        if key in data:
            return data[key]
        return None

    def gps_to_degrees(self, value):
        """
        Converts the GPS coordinates of the EXIF metadata into readable
        degrees, minutes and seconds GPS coordinates
        """
        d = float(value[0])

        m = float(value[1])

        s = float(value[2])

        return d + (m/60.0) + (s/3600.0)

    def get_lat_lon(self):
        """Returns the latitude and longitude if available in the exif data"""

        lat = None
        lon = None
        exif_data = self.get_exif_data()

        if 'GPSInfo' in exif_data:
            gps_info = exif_data['GPSInfo']
            gps_latitude = self.get_if_exist(gps_info, 'GPSLatitude')
            gps_latitude_ref = self.get_if_exist(gps_info, 'GPSLatitudeRef')
            gps_longitude = self.get_if_exist(gps_info, 'GPSLongitude')
            gps_longitude_ref = self.get_if_exist(gps_info, 'GPSLongitudeRef')

            if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
                lat = self.gps_to_degrees(gps_latitude)
                if gps_latitude_ref != 'N':
                    lat = -lat

                lon = self.gps_to_degrees(gps_longitude)
                if gps_longitude_ref != 'E':
                    lon = - lon

        return lat, lon
