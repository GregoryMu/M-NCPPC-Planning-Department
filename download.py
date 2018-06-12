# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# download.py
# Created on: 2018-06-12 3:48:16.00000
#   
# Description: Downloads the current OSM data for the state of Maryland and extracts it to a folder
# ---------------------------------------------------------------------------

# Import 
import requests, zipfile, StringIO, arcpy

url = "http://download.geofabrik.de/north-america/us/maryland-latest-free.shp.zip"

r = requests.get(url, stream = True)
z = zipfile.ZipFile(StringIO.StringIO(r.content))
z.extractall("C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\maryland-latest-free.shp")

print "Files Extracted"
