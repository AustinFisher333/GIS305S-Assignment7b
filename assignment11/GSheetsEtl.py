from SpatialEtl import SpatialEtl

class GSheetsEtl(SpatialEtl):
    def __init__(self, remote, local_dir, data_format, destination):
        super().__init__(remote, local_dir, data_format, destination)

    def process(self):
        self.extract()
        self.transform()
        self.load()
