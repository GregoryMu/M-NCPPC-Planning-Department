# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# buildingMergeByWSSCGrid.py
# Created on: 2018-06-07 15:12:10.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: buildingMergeByWSSCGrid <Expression> <buildingX_SpatialJoin_shp> 
# Description: This script will take an input of buildings and address points
#              and clip to to much smaller sizes using the WSSC Grid.
#              Next it will join these two shapefiles so that each building will
#              have an address point associated with it.  It also fixes fields
#              towards the proper OSM standards for tagging
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

print "Beginning Clipping"

# Local variables (path for Building shapefile, WSSC Grid Shapefile, Address Point shapefile, and Existing Building shapefile):
Building_2014_Py_shp = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\Projected\\Building_2014_Py.shp"
WSSC_Grid = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\Projected\\WSSC_Grid.shp"
Address_Pt_shp = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\Projected\\Address_Pt.shp"
Existing_Building_shp = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\OSM_PG\\buildings.shp"

# Set Geoprocessing environments
arcpy.env.scratchWorkspace = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace"
arcpy.env.workspace = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace"
arcpy.env.overwriteOutput = True

# Variables to run while loop for each grid
x = 0
rows = int(arcpy.GetCount_management(WSSC_Grid).getOutput(0))

# Initial variables to initiate loop
Expression = "\"FID\" = " + str(x)
buildingX_SpatialJoin_shp = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\buildingsX\\building_join\\building" + str(x) + "_SpatialJoin.shp"
wsscX_shp = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\buildingsX\\temp\\wssc" + str(x) + ".shp"
buildingX_shp = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\buildingsX\\temp\\building" + str(x) + ".shp"
addrX_shp = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\buildingsX\\temp\\addr" + str(x) + ".shp"
existX_shp = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\buildingsX\\temp\\exist" + str(x) + ".shp"
intersectX_shp = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\buildingsX\\intersect\\intersect" + str(x) + ".shp"
newX_shp = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\buildingsX\\new\\new" + str(x) + ".shp"

print "Starting Loop"

# Loop runs through each grid
while (x < rows):
    Expression = "\"FID\" = " + str(x)
    buildingX_SpatialJoin_shp = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\buildingsX\\building_join\\building" + str(x) + "_SpatialJoin.shp"
    wsscX_shp = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\buildingsX\\temp\\wssc" + str(x) + ".shp"
    buildingX_shp = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\buildingsX\\temp\\building" + str(x) + ".shp"
    addrX_shp = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\buildingsX\\temp\\addr" + str(x) + ".shp"
    existX_shp = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\buildingsX\\temp\\exist" + str(x) + ".shp"
    intersectX_shp = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\buildingsX\\intersect\\intersect" + str(x) + ".shp"
    newX_shp = "C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\buildingsX\\new\\new" + str(x) + ".shp"
    # Selects a single grid and clips buildings, addresses, and existing buildings to that grid
    arcpy.Select_analysis(WSSC_Grid, wsscX_shp, Expression)
    arcpy.MakeFeatureLayer_management(Building_2014_Py_shp, "Building_2014_Py_shp")
    arcpy.SelectLayerByLocation_management("Building_2014_Py_shp", "INTERSECT", wsscX_shp, "", "NEW_SELECTION", "NOT_INVERT")
    arcpy.CopyFeatures_management("Building_2014_Py_shp", buildingX_shp)
    arcpy.Clip_analysis(Address_Pt_shp, wsscX_shp, addrX_shp, "")
    arcpy.MakeFeatureLayer_management(Existing_Building_shp, "buildings_shp")
    arcpy.SelectLayerByLocation_management("buildings_shp", "INTERSECT", wsscX_shp, "", "NEW_SELECTION", "NOT_INVERT")
    arcpy.CopyFeatures_management("buildings_shp", existX_shp, "", "0", "0", "0")
    # Joins building and address clipped shapefiles
    arcpy.SpatialJoin_analysis(buildingX_shp, addrX_shp, buildingX_SpatialJoin_shp, "JOIN_ONE_TO_ONE", "KEEP_ALL", "COMPLETE_A \"COMPLETE_A\" true true false 27 Text 0 0 ,First,#,C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\buildingsX\\temp\\addr" + str(x) + ".shp,COMPLETE_A,-1,-1;COMPLETE_S \"COMPLETE_S\" true true false 151 Text 0 0 ,First,#,C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\buildingsX\\temp\\addr" + str(x) + ".shp,COMPLETE_S,-1,-1;COMPLETE_1 \"COMPLETE_1\" true true false 96 Text 0 0 ,First,#,C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\buildingsX\\temp\\addr" + str(x) + ".shp,COMPLETE_1,-1,-1;PLACE_NAME \"PLACE_NAME\" true true false 30 Text 0 0 ,First,#,C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\buildingsX\\temp\\addr" + str(x) + ".shp,PLACE_NAME,-1,-1;STATE_NAME \"STATE_NAME\" true true false 2 Text 0 0 ,First,#,C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\buildingsX\\temp\\addr" + str(x) + ".shp,STATE_NAME,-1,-1;ZIP_CODE \"ZIP_CODE\" true true false 5 Text 0 0 ,First,#,C:\\Users\\Gregory.mulea\\Documents\\ArcGIS\\Workspace\\buildingsX\\temp\\addr" + str(x) + ".shp,ZIP_CODE,-1,-1", "INTERSECT", "", "")
    # Edits tags (deletes auto field JoinCount, Adds two fields for OSM tags: building=yes and source=M-NCPPC,
    # and reformats address fields from all caps to only caps on first letter of each word
    arcpy.DeleteField_management(buildingX_SpatialJoin_shp, ["Join_Count", "TARGET_FID"])
    arcpy.AddField_management(buildingX_SpatialJoin_shp, "building", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.CalculateField_management(buildingX_SpatialJoin_shp, "building", "\"yes\"", "PYTHON_9.3", "")
    arcpy.AddField_management(buildingX_SpatialJoin_shp, "source", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    arcpy.CalculateField_management(buildingX_SpatialJoin_shp, "source", "\"M-NCPPC\"", "PYTHON_9.3", "")
    arcpy.CalculateField_management(buildingX_SpatialJoin_shp, "COMPLETE_S", "!COMPLETE_S!.title()", "PYTHON_9.3", "")
    arcpy.CalculateField_management(buildingX_SpatialJoin_shp, "COMPLETE_1", "!COMPLETE_1!.title()", "PYTHON_9.3", "")
    arcpy.CalculateField_management(buildingX_SpatialJoin_shp, "PLACE_NAME", "!PLACE_NAME!.title()", "PYTHON_9.3", "")
    # Checks for existing buildings and outputs both existing buildings and new buildings
    arcpy.Intersect_analysis([existX_shp, buildingX_SpatialJoin_shp], intersectX_shp)
    arcpy.MakeFeatureLayer_management(buildingX_SpatialJoin_shp, "building" + str(x) + "_SpatialJoin_shp")
    arcpy.SelectLayerByLocation_management("building" + str(x) + "_SpatialJoin_shp", "INTERSECT", intersectX_shp, "", "NEW_SELECTION", "INVERT")
    arcpy.CopyFeatures_management("building" + str(x) + "_SpatialJoin_shp", newX_shp)
    # Deletes the placeholder clipped files in order to minimize clutter
    arcpy.Delete_management(wsscX_shp)
    arcpy.Delete_management(buildingX_shp)
    arcpy.Delete_management(addrX_shp)
    arcpy.Delete_management(existX_shp)
    # Print value to keep track of the progress of the script
    print x
    # Increments x value by one
    x += 1
