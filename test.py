# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# test.py
# Created on: 2018-06-15 13:15:47.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
building5 = "building5"
addr5 = "addr5"
TEST5_shp = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\TEST5.shp"

# Process: Spatial Join
arcpy.SpatialJoin_analysis(building5, addr5, TEST5_shp, "JOIN_ONE_TO_ONE", "KEEP_ALL", "COMPLETE_A \"COMPLETE_A\" true true false 27 Text 0 0 ,First,#,addr5,COMPLETE_A,-1,-1;COMPLETE_S \"COMPLETE_S\" true true false 151 Text 0 0 ,First,#,addr5,COMPLETE_S,-1,-1;COMPLETE_1 \"COMPLETE_1\" true true false 96 Text 0 0 ,First,#,addr5,COMPLETE_1,-1,-1;PLACE_NAME \"PLACE_NAME\" true true false 30 Text 0 0 ,First,#,addr5,PLACE_NAME,-1,-1;STATE_NAME \"STATE_NAME\" true true false 2 Text 0 0 ,First,#,addr5,STATE_NAME,-1,-1;ZIP_CODE \"ZIP_CODE\" true true false 5 Text 0 0 ,First,#,addr5,ZIP_CODE,-1,-1", "INTERSECT", "", "")

