# Picture Sorting by Geolocation

This repo contains a script to organize a folder of pictures insider folders sorted by geolocation.

Given a folder of pictures taken with a smartphone of digital camera with geotagging turned on, extract the `GPSInfo` from each picture.

This GPS information is then used to extract the location of interest (address, city, state, country and etc.) and then organize the given pictures in respective folders sorted by the desired geolocation information (default is country in this repo).

[pyheif](https://pypi.org/project/pyheif/)\
[geopy](https://geopy.readthedocs.io/en/stable/)

### References

[gitmp01/heic2jpeg](https://github.com/gitmp01/heic2jpeg/blob/master/heic-to-jpeg.py)