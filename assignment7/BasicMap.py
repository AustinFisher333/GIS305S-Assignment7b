class BasicMap:
    """
    A simple map class.
    All maps have a center longitude and latitude
    All maps have a width and height
    """

    # initializer with instance attributes
    def __init__(self, long, lat, width, height):
        """
        Construct a new 'BasicMap' object.

        :param long: The longitude of the center point of the map
        :param lat: The latitude of the center point of the map
        :param width: The width of the map
        :param height: The height of the map

        :return: returns nothing
        """
        self.long = long
        self.lat = lat
        self.width = width
        self.height = height

    def describe(self):
        """
        Describe the details of the map.

        :return: returns nothing
        """
        print(f"Center longitude: {self.long}")
        print(f"Center latitude: {self.lat}")
        print(f"Width in DD: {self.width}")
        print(f"Height in DD: {self.height}")

    def get_bounds(self):
        """
        Describe the boundaries of the map.

        :return: returns nothing
        """
        try:
            # Convert values to float in case they were entered as strings
            lat = float(self.lat)
            long = float(self.long)
            width = float(self.width)
            height = float(self.height)

            north = lat + height
            east = long + width
            south = lat - height
            west = long - width

            print(f"North: {north}")
            print(f"East: {east}")
            print(f"South: {south}")
            print(f"West: {west}")

        except ValueError:
            print("Error: Invalid input type! Longitude, latitude, width, and height must be numbers.")

if __name__ == "__main__":
    # Create an instance with string values (this is incorrect)
    my_map = BasicMap("-105.2705", "40.015", "0.5", "0.25")
    my_map.describe()

    print('Calculating bounds...')
    try:
        my_map.get_bounds()
    except TypeError:
        print("Error: in get_bounds - input values must be numbers!")
