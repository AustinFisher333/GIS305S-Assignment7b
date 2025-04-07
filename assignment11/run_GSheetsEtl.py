from GSheetsEtl import GSheetsEtl

# Update these to your actual paths
remote = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTDjitOlmILea7koCORJkq6QrUcwBJM7K3vy4guXB0mU_nWR6wsPn136bpH6ykoUxyYMW7wTwkzE37l/pub?output=csv"
local_dir = r"C:\Users\valen\Downloads"
data_format = "csv"
destination = r"C:\Users\valen\Documents\ArcGIS\GIS305\GeoSpatial Programming\westnileoutbreak\WestNileOutbreak\WestNileOutbreak.gdb"

etl = GSheetsEtl(remote, local_dir, data_format, destination)
etl.process()
