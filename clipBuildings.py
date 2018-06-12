# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# download.py
# Created on: 2018-06-12 3:48:16.00000
#   
# Description: 
# ---------------------------------------------------------------------------

# Import 
import arcpy

existingBuildings = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\maryland-latest-free.shp\\gis_osm_buildings_a_free_1.shp"
buildings = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\OSM_PG\\buildings.shp"
county = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\County.shp"

if arcpy.Exists(buildings):
    arcpy.Delete_management(buildings)

arcpy.Clip_analysis(existingBuildings, county, buildings)
