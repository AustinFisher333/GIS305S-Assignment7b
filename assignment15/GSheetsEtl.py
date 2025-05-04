from SpatialEtl import SpatialEtl

class GSheetsEtl(SpatialEtl):
    """
    GSheetsEtl performs an extract, transform and load process using a URL to a Google spreadsheet.
    The spreadsheet must contain an address and ZIP code column.

    Parameters:
    config_dict (dictionary): A dictionary with keys: 'remote', 'local_dir', 'data_format', and 'destination'.
    """

    def __init__(self, config_dict):
        """
        Initialize the ETL class with a configuration dictionary.

        Parameters:
        config_dict (dict): Should include 'remote', 'local_dir', 'data_format', 'destination'
        """
        remote = config_dict.get("remote")
        local_dir = config_dict.get("local_dir")
        data_format = config_dict.get("data_format")
        destination = config_dict.get("destination")

        super().__init__(remote, local_dir, data_format, destination)

    def extract(self):
        """
        Extract data from the Google spreadsheet and save it as a local CSV file.
        """
        print("Custom GSheetsEtl.extract() called")
