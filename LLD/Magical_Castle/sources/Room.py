from CustomExceptions import InvalidDirectionException

class Room:
    """
        Object of this class represent room in castle.
    """
    def __init__(self, ID = 0, north = 0, south = 0, east = 0, west = 0, portal = False, wormhole = False, diamond = None) -> None:
        """
        creates and returns a Room object.
        """

        self.ID = ID
        self.north = int(north)
        self.south = int(south)
        self.east = int(east)
        self.west = int(west)
        self.portal = portal
        self.wormhole = wormhole
        self.diamond = diamond
        self.is_there_entrance_exit = False

    def get_id(self):
        return self.ID
    def set_id(self, ID):
        self.ID = ID

    def get_portal(self):
        return self.portal
    def set_portal(self, portal):
        self.portal = portal

    def get_wormhole(self):
        return self.wormhole
    def set_wormhole(self, wormhole):
        self.wormhole = wormhole

    def get_diamond(self):
        return self.diamond
    def set_diamond(self, diamond):
        self.diamond = diamond

    def get_door(self, direction):
        if direction == "north":
            return self.north
        elif direction == "south":
            return self.south
        elif direction == "east":
            return self.east
        elif direction == "west":
            return self.west
        else:
            raise InvalidDirectionException()

    def set_link(self, direction, val):
        self.direction = val

    def is_there_entrance_exit_door(self):
        return self.is_there_entrance_exit

    def __str__(self):
        # return " Room : {} {} ".format(self.ID, self.portal, self.wormhole)
        return " Room: {} | North : {} | South : {} | East : {} | West : {}"\
                    .format(self.ID, self.north,self.south,self.west,self.east)