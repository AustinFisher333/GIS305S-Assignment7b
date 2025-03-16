import arcpy
import os

def intersect(layer_list, output_layer):
    """
    Run an intersect analysis between the two buffer layers.
    :param layer_list: List of layers to intersect
    :param output_layer: Path for the output intersect layer
    """
    try:
        # If output layer already exists, delete it
        if arcpy.Exists(output_layer):
            arcpy.Delete_management(output_layer)
            arcpy.AddMessage(f"Existing intersect layer deleted: {output_layer}")

        arcpy.Intersect_analysis(layer_list, output_layer)
        arcpy.AddMessage(f"New intersect layer generated: {output_layer}")
    except arcpy.ExecuteError:
        arcpy.AddError(f"Failed to run Intersect_analysis for {output_layer}")


def buffer_layer(input_gdb, input_layer, dist):
    """
    Run a buffer analysis on the input_layer with a user-specified distance.
    :param input_gdb: The geodatabase where the input layer is stored
    :param input_layer: The layer to buffer
    :param dist: The buffer distance
    :return: Path to the output buffered layer
    """
    try:
        # Convert distance to float
        dist = float(dist)
        dist = f"{dist} miles"  # Append "miles" unit

        # Construct input and output layer paths
        buf_layer = os.path.join(input_gdb, input_layer)
        output_layer = os.path.join(input_gdb, f"{input_layer}_buf")

        # If buffer layer already exists, delete it
        if arcpy.Exists(output_layer):
            arcpy.Delete_management(output_layer)
            arcpy.AddMessage(f"Existing buffer layer deleted: {output_layer}")

        # Perform buffer analysis
        arcpy.Buffer_analysis(buf_layer, output_layer, dist, "FULL", "ROUND", "ALL")
        arcpy.AddMessage(f"Buffer layer created: {output_layer}")
        return output_layer

    except ValueError:
        arcpy.AddError(f"Invalid distance value for {input_layer}. Please enter a valid number.")
        return None
    except arcpy.ExecuteError:
        arcpy.AddError(f"Failed to buffer {input_layer}.")
        return None


def main():
    """
    Main function to execute the geoprocessing workflow.
    """
    # Define workspace
    arcpy.env.workspace = r"C:\Users\valen\Documents\ArcGIS\GIS305\Projects\ModelBuilder\ModelBuilder.gdb"
    arcpy.env.overwriteOutput = True

    # Define input geodatabase
    input_gdb = r"C:\Users\valen\Documents\ArcGIS\GIS305\GeoSpatial Programming\Week1\b1\Data\Admin\Admin\AdminData.gdb"

    # Get user inputs using GetParameterAsText()
    dist_cities = arcpy.GetParameterAsText(0)
    dist_rivers = arcpy.GetParameterAsText(1)

    # **Hardcode the output layer name**
    intersect_lyr_name = "Cities_Rivers_Intersect2"

    # Validate input distances
    if not dist_cities or not dist_rivers:
        arcpy.AddError("Buffer distance values are required!")
        return

    # Run buffer analyses
    buf_cities = buffer_layer(input_gdb, "cities", dist_cities)
    buf_rivers = buffer_layer(input_gdb, "us_rivers", dist_rivers)

    # Ensure buffers were created before proceeding
    if buf_cities and buf_rivers:
        output_intersect = os.path.join(arcpy.env.workspace, intersect_lyr_name)
        lyr_list = [buf_rivers, buf_cities]
        intersect(lyr_list, output_intersect)

        # Load into ArcGIS project
        try:
            aprx_path = r"C:\Users\valen\OneDrive\Documents\ArcGIS\Projects\ModelBuilder\ModelBuilder.aprx"
            aprx = arcpy.mp.ArcGISProject(aprx_path)

            # Check if maps exist before adding the layer
            maps = aprx.listMaps()
            if maps:
                map_doc = maps[0]  # Use the first available map
                map_doc.addDataFromPath(output_intersect)
                aprx.save()
                arcpy.AddMessage(f"Intersect layer added to project: {intersect_lyr_name}")
            else:
                arcpy.AddError("No maps found in the project. Could not add the layer.")

        except Exception as e:
            arcpy.AddError(f"Failed to add layer to ArcGIS project: {str(e)}")


if __name__ == '__main__':
    main()
'Had some issues with this code because of read/write permissions'